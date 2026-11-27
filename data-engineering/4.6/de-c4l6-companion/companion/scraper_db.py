#!/usr/bin/env python3
"""سكرابر مجدول بيخزن في SQLite: يسحب أول صفحة اقتباسات ويخزنها.
كل تشغيلة بتسجل في logs/scraper.log وبتضيف صف في جدول runs
وبتخزن الاقتباسات الجديدة بس في جدول quotes (UNIQUE بيمنع التكرار).
"""
import logging
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "quotes.db"
URL = "https://quotes.toscrape.com/"
HEADERS = {"User-Agent": "mahara-course-demo/1.0 (+training; contact: replace-with-your-own-email)"}

LOG_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "scraper.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("db_scraper")

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    run_id       INTEGER PRIMARY KEY,
    run_at_utc   TEXT NOT NULL,
    status       TEXT NOT NULL,
    quotes_found INTEGER NOT NULL DEFAULT 0,
    quotes_new   INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS quotes (
    quote_id INTEGER PRIMARY KEY,
    run_id   INTEGER NOT NULL REFERENCES runs(run_id),
    text     TEXT NOT NULL,
    author   TEXT NOT NULL,
    UNIQUE(text, author)
);
"""


def main() -> int:
    log.info("run started")
    time.sleep(0.3)  # فاصل مهذب قبل الطلب (درس 4)
    resp = requests.get(URL, headers=HEADERS, timeout=10)
    log.info("fetch status=%s bytes=%s", resp.status_code, len(resp.content))
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    quotes = [
        (q.select_one("span.text").get_text(strip=True),
         q.select_one("small.author").get_text(strip=True))
        for q in soup.select("div.quote")
    ]
    if not quotes:
        raise RuntimeError("no quotes found on page")

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")  # افتراضها ممكن يختلف حسب بناء المكتبة، فبنفعلها صراحة ونتحقق منها في كل اتصال
    with conn:  # commit تلقائي عند النجاح وrollback عند أي خطأ
        conn.executescript(SCHEMA)
        cur = conn.execute(
            "INSERT INTO runs (run_at_utc, status, quotes_found) VALUES (?, 'ok', ?)",
            (ts, len(quotes)),
        )
        run_id = cur.lastrowid
        before = conn.total_changes
        conn.executemany(
            "INSERT INTO quotes (run_id, text, author) VALUES (?, ?, ?)"
            " ON CONFLICT(text, author) DO NOTHING",
            [(run_id, t, a) for t, a in quotes],
        )
        new = conn.total_changes - before
        conn.execute("UPDATE runs SET quotes_new = ? WHERE run_id = ?", (new, run_id))
    conn.close()

    log.info("run_id=%s stored quotes=%s new=%s db=%s", run_id, len(quotes), new, DB_PATH)
    log.info("run finished ok")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        log.exception("run failed")
        sys.exit(1)
