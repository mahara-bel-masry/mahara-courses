# solutions.py
# DE Course 4 - Lesson 2 - executed solutions for the lesson's exercises
# Same safe get_soup as the lesson: status 200 + expected marker, else halt.
# Target: books.toscrape.com

import csv, time, requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"

def get_soup(url, marker):
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        print("stop: status", r.status_code, "- not 200 (429/5xx mean the site wants us to stop)")
        raise SystemExit(1)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    if not soup.select(marker):
        print("stop: status 200 but expected marker missing:", marker)
        raise SystemExit(1)
    return soup, r

def extract(pod, url, with_rating=False):
    a = pod.select_one("h3 a")
    raw = pod.select_one("p.price_color").get_text(strip=True)
    price = float(raw.replace("£", ""))
    if with_rating:
        rating = [c for c in pod.select_one("p.star-rating")["class"] if c != "star-rating"][0]
        return (a["title"], price, rating, urljoin(url, a["href"]))
    return (a["title"], price, urljoin(url, a["href"]))

def scrape(max_pages, with_rating=False):
    rows, url, page = [], BASE, 0
    while url and page < max_pages:
        page += 1
        soup, r = get_soup(url, "article.product_pod")
        for pod in soup.select("article.product_pod"):
            rows.append(extract(pod, url, with_rating))
        nxt = soup.select_one("li.next a")
        url = urljoin(url, nxt["href"]) if nxt else None
        if url and page < max_pages:
            time.sleep(1)
    return rows

print("=== Exercise 1: extend the scraper to 5 pages ===")
rows5 = scrape(5)
print("rows from 5 pages:", len(rows5))
time.sleep(1)

print("=== Exercise 2: add the rating column ===")
rows_r = scrape(3, with_rating=True)
with open("books_with_rating.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["title", "price_gbp", "rating", "url"])
    w.writerows(rows_r)
print("rows:", len(rows_r), "| first:", rows_r[0])

print("=== Exercise 3: count books cheaper than 20 in the first 3 pages ===")
cheap = [r for r in rows_r if r[1] < 20]
print("books under 20 gbp:", len(cheap))

print("=== Exercise 4: save them sorted by price, ascending ===")
cheap_sorted = sorted(cheap, key=lambda r: r[1])
with open("cheap_books.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["title", "price_gbp", "rating", "url"])
    w.writerows(cheap_sorted)
print("cheapest:", cheap_sorted[0][:2])
print("most expensive within cheap:", cheap_sorted[-1][:2])
