# scraper.py
# DE Course 4 - Lesson 2 - the full first scraper from the lesson
# Bounded training run: first 3 pages of books.toscrape.com (60 books).
# The same loop can follow next to the last page, after you learn each
# site's limits and rules (robots.txt, terms, rate) in lesson 4.
# Needs: requests, beautifulsoup4  ->  pip install requests beautifulsoup4

import csv, time, requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"
MAX_PAGES = 3          # bounded training run, not full-site coverage

def get_soup(url, marker):
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        # 429/5xx: the site asked us to stop - this starter halts, no retry
        print("stop: status", r.status_code, "- not 200 (429/5xx mean the site wants us to stop)")
        raise SystemExit(1)
    r.encoding = "utf-8"            # server sends no charset (lesson 1 trap)
    soup = BeautifulSoup(r.text, "html.parser")
    if not soup.select(marker):
        print("stop: status 200 but expected marker missing:", marker)
        raise SystemExit(1)
    return soup, r

def extract(pod, url):
    a = pod.select_one("h3 a")
    raw = pod.select_one("p.price_color").get_text(strip=True)
    return (a["title"], float(raw.replace("£", "")), urljoin(url, a["href"]))

rows, url, page = [], BASE, 0
while url and page < MAX_PAGES:
    page += 1
    soup, r = get_soup(url, "article.product_pod")
    for pod in soup.select("article.product_pod"):
        rows.append(extract(pod, url))
    print(f"page {page}: status {r.status_code}, books so far: {len(rows)}")
    nxt = soup.select_one("li.next a")
    url = urljoin(url, nxt["href"]) if nxt else None
    if url and page < MAX_PAGES:
        time.sleep(1)   # our choice for this training run, not a general rule

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["title", "price_gbp", "url"])
    w.writerows(rows)

print("total rows:", len(rows))
print("saved to books.csv")
