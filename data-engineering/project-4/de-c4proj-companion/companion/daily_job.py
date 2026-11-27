#!/usr/bin/env python3
# مشروع كورس 4: سكرابر مجدول يجمع أسعار الكتب يوميًا، يخزنها في SQLite، ويبعت ملخص يومي
# التشغيل: python3 daily_job.py
import logging
import sqlite3
import time
import sys
import smtplib
from datetime import datetime, timezone
from email.mime.text import MIMEText
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
TOTAL_PAGES = 50
DELAY_SECONDS = 1  # احترام معدل الطلبات: ثانية بين كل صفحة والتانية
DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "books.db"
SMTP_HOST = "localhost"   # في العرض: خادم محلي للتجربة. في الحقيقة: smtp.gmail.com مثلًا مع بيانات حسابك
SMTP_PORT = 1025
MAIL_FROM = "scraper@localhost"
MAIL_TO = "me@localhost"

LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "daily_job.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("daily_job")

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
  run_id     INTEGER PRIMARY KEY,
  run_at_utc TEXT NOT NULL,
  status     TEXT NOT NULL,
  pages_ok   INTEGER NOT NULL DEFAULT 0,
  books_found INTEGER NOT NULL DEFAULT 0,
  books_new  INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS books (
  book_key        TEXT PRIMARY KEY,
  title      TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS snapshots (
  run_id     INTEGER NOT NULL REFERENCES runs(run_id),
  book_key        TEXT NOT NULL REFERENCES books(book_key),
  price_gbp  REAL NOT NULL,
  rating     INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
  PRIMARY KEY (run_id, book_key)
);
"""

RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_all():
    """يجلب الخمسين صفحة واحدة واحدة باحترام معدل الطلبات ويرجع قايمة الكتب."""
    books = []
    headers = {"User-Agent": "SkillBuildCourse/1.0 (educational demo)"}
    for page in range(1, TOTAL_PAGES + 1):
        url = BASE_URL.format(page)
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        r.encoding = "utf-8"  # الموقع بيبعت الصفحة utf-8 من غير ما يصرح، فبنحدد الترميز صراحة
        soup = BeautifulSoup(r.text, "html.parser")
        pods = soup.select("article.product_pod")
        for pod in pods:
            title = pod.h3.a["title"].strip()
            price = float(pod.select_one("p.price_color").text.replace("£", "").strip())
            rating_word = pod.select_one("p.star-rating")["class"][1]
            book_key = pod.h3.a["href"].split("/")[-2]
            books.append({"book_key": book_key, "title": title, "price": price, "rating": RATING_WORDS[rating_word]})
        log.info("page %d ok books_so_far=%d", page, len(books))
        if page < TOTAL_PAGES:
            time.sleep(DELAY_SECONDS)
    return books


def store(conn, run_id, books):
    """يخزن التشغيلة: كتاب جديد يتسجل، ونسخة السعر بتتربط بالتشغيلة."""
    new_count = 0
    for b in books:
        cur = conn.execute(
            "INSERT INTO books (book_key, title) VALUES (?, ?) ON CONFLICT(book_key) DO NOTHING",
            (b["book_key"], b["title"]),
        )
        new_count += cur.rowcount
        conn.execute(
            "INSERT INTO snapshots (run_id, book_key, price_gbp, rating) VALUES (?, ?, ?, ?)",
            (run_id, b["book_key"], b["price"], b["rating"]),
        )
    return new_count


def build_summary(conn, run_id):
    """يبني نص الملخص اليومي من القاعدة، ومقارنة أسعار بآخر تشغيلة قبلها."""
    total_books = conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]
    # التشغيلات المكتملة قبل دي + الحالية: الملخص ده هو آخر خطوة قبل ما تتعلم ok
    total_runs = conn.execute("SELECT COUNT(*) FROM runs WHERE status='ok'").fetchone()[0] + 1
    avg_price = conn.execute(
        "SELECT ROUND(AVG(price_gbp), 2) FROM snapshots WHERE run_id = ?", (run_id,)
    ).fetchone()[0]
    cheapest = conn.execute(
        """SELECT b.title, s.price_gbp FROM snapshots s JOIN books b USING (book_key)
           WHERE s.run_id = ? ORDER BY s.price_gbp ASC LIMIT 5""", (run_id,),
    ).fetchall()
    priciest = conn.execute(
        """SELECT b.title, s.price_gbp FROM snapshots s JOIN books b USING (book_key)
           WHERE s.run_id = ? ORDER BY s.price_gbp DESC LIMIT 5""", (run_id,),
    ).fetchall()
    dist = conn.execute(
        "SELECT rating, COUNT(*) FROM snapshots WHERE run_id = ? GROUP BY rating ORDER BY rating",
        (run_id,),
    ).fetchall()
    prev = conn.execute(
        "SELECT MAX(run_id) FROM runs WHERE status='ok' AND run_id < ?", (run_id,)
    ).fetchone()[0]
    changes = []
    if prev is not None:
        changes = conn.execute(
            """SELECT b.title, p.price_gbp, s.price_gbp
               FROM snapshots s
               JOIN snapshots p ON p.book_key = s.book_key AND p.run_id = ?
               JOIN books b USING (book_key)
               WHERE s.run_id = ? AND s.price_gbp <> p.price_gbp""",
            (prev, run_id),
        ).fetchall()

    lines = [
        "ملخص أسعار الكتب اليومي",
        "=" * 30,
        f"التشغيلة رقم: {run_id}",
        f"إجمالي الكتب المتتبعة: {total_books}",
        f"متوسط السعر في لقطة النهارده: {avg_price} جنيه إسترليني",
        f"توزيع التقييمات: " + "، ".join(f"{n} نجوم: {c}" for n, c in dist),
        "",
        "أرخص 5 كتب:",
        *[f"  - {t[:50]} : {p}" for t, p in cheapest],
        "أغلى 5 كتب:",
        *[f"  - {t[:50]} : {p}" for t, p in priciest],
        "",
    ]
    if prev is None:
        lines.append("أول تشغيلة: مفيش مقارنة أسعار بيوم سابق لسه.")
    elif changes:
        lines.append(f"تغيرات الأسعار عن التشغيلة {prev}:")
        lines += [f"  - {t[:45]} : كان {old} بقى {new}" for t, old, new in changes]
    else:
        lines.append(f"مفيش أي تغير في الأسعار عن التشغيلة {prev}.")
    lines.append(f"إجمالي التشغيلات الناجحة لحد دلوقتي: {total_runs}")
    return "\n".join(lines)


def send_summary(subject, body):
    """يبعت الملخص إيميل عبر SMTP. في العرض خادم محلي بيطبع اللي يوصله."""
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = MAIL_FROM
    msg["To"] = MAIL_TO
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
        smtp.send_message(msg)
    log.info("summary email sent to %s:%s", SMTP_HOST, SMTP_PORT)


def main():
    log.info("daily job started")
    DATA_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    # افتراضها ممكن يختلف حسب بناء المكتبة، فبنفعلها صراحة في كل اتصال ونتأكد إنها اتفعلت فعلًا
    conn.execute("PRAGMA foreign_keys = ON")
    if conn.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
        raise RuntimeError("SQLite build without working foreign key enforcement; refusing to run unguarded")
    try:
        with conn:
            conn.executescript(SCHEMA)
            run_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            cur = conn.execute(
                "INSERT INTO runs (run_at_utc, status) VALUES (?, 'started')", (run_at,)
            )
            run_id = cur.lastrowid
        books = scrape_all()
        with conn:
            new_count = store(conn, run_id, books)
            # التخزين مؤقت لحد ما سير العملية كله يكمل: التشغيلة لسه started
            conn.execute(
                "UPDATE runs SET pages_ok=?, books_found=?, books_new=? WHERE run_id=?",
                (TOTAL_PAGES, len(books), new_count, run_id),
            )
        log.info("run_id=%d stored books=%d new=%d (provisional)", run_id, len(books), new_count)
        summary = build_summary(conn, run_id)
        log.info("summary built (%d chars)", len(summary))
        send_summary(f"ملخص الكتب اليومي - تشغيلة {run_id}", summary)
        # ok معناها سير العملية كله نجح: جلب وتخزين وملخص وإرسال
        with conn:
            conn.execute("UPDATE runs SET status='ok' WHERE run_id=?", (run_id,))
        log.info("daily job finished ok")
        return 0
    except Exception:
        log.exception("daily job failed")
        try:
            with conn:
                conn.execute("UPDATE runs SET status='failed' WHERE run_id=?", (run_id,))
        except Exception:
            log.exception("could not mark run as failed")
        return 1
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
