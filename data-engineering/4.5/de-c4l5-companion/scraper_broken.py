#!/usr/bin/env python3
"""سكرابر مجدول: يسحب أول صفحة اقتباسات ويسجل النتيجة.
كل تشغيلة بتسجل سطر في logs/scraper.log وبتضيف صف في data/quotes_log.csv
"""
import csv
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"
URL = "https://quotes.toscrape.invalid/"
HEADERS = {"User-Agent": "mahara-course-demo/1.0 (+training; contact: replace-with-your-own-email)"}

LOG_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "scraper.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("scheduled_scraper")


def main() -> int:
    log.info("run started")
    time.sleep(0.3)  # فاصل مهذب قبل الطلب (درس 4)
    resp = requests.get(URL, headers=HEADERS, timeout=10)
    log.info("fetch status=%s bytes=%s", resp.status_code, len(resp.content))
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    quotes = soup.select("div.quote")
    if not quotes:
        raise RuntimeError("no quotes found on page")

    first = quotes[0].select_one("span.text").get_text(strip=True)
    author = quotes[0].select_one("small.author").get_text(strip=True)
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")

    csv_path = DATA_DIR / "quotes_log.csv"
    new_file = not csv_path.exists()
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["run_at_utc", "quotes_count", "first_quote", "author"])
        w.writerow([ts, len(quotes), first, author])

    log.info("saved quotes=%s to %s", len(quotes), csv_path)
    log.info("run finished ok")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        log.exception("run failed")
        sys.exit(1)
