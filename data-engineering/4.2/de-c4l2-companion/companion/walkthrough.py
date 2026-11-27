# walkthrough.py
# DE Course 4 - Lesson 2 - executed walkthrough of lesson 1's five exercises
# Every page is checked before parsing: status 200 AND an expected-content
# marker. If either fails the script stops with a clear message.
# Target: books.toscrape.com

import time, requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"

def get_soup(url, marker):
    # Parse the HTML into a tree to CHECK the expected marker first;
    # only extract fields after both checks pass.
    r = requests.get(url, timeout=30)
    print("status:", r.status_code)
    if r.status_code != 200:
        print("stop: not 200 (429/5xx mean the site wants us to stop)")
        raise SystemExit(1)
    r.encoding = "utf-8"   # server sends no charset (lesson 1 trap)
    soup = BeautifulSoup(r.text, "html.parser")
    if not soup.select(marker):
        print("stop: 200 but expected marker missing:", marker)
        raise SystemExit(1)
    print("200 and expected marker found:", marker)
    return soup, r

print("=== Exercise 1: status AND content marker before extracting ===")
url_book = BASE + "catalogue/a-light-in-the-attic_1000/index.html"
soup1, _ = get_soup(url_book, "div.product_main")
time.sleep(1)

print("=== Exercise 2: book detail fields ===")
soup, _ = get_soup(url_book, "div.product_main")
print("h1:", soup.select_one("div.product_main h1").get_text(strip=True))
print("price:", soup.select_one("div.product_main p.price_color").get_text(strip=True))
print("availability:", soup.select_one("div.product_main p.instock.availability").get_text(strip=True))
print("UPC:", soup.select_one("table.table.table-striped td").get_text(strip=True))
time.sleep(1)

print("=== Exercise 3: star rating of second book on home ===")
home, _ = get_soup(BASE, "article.product_pod")
second = home.select("article.product_pod")[1]
rating = [c for c in second.select_one("p.star-rating")["class"] if c != "star-rating"][0]
print("second book:", second.select_one("h3 a")["title"], "| rating:", rating)

print("=== Exercise 4: categories ===")
cats = [c.get_text(strip=True) for c in home.select("ul.nav-list ul li a")]
print("count:", len(cats))
print("first5:", cats[:5])
print("last5:", cats[-5:])
time.sleep(1)

print("=== Exercise 5: follow next to page 2 ===")
nxt = home.select_one("li.next a")["href"]
p2, r2 = get_soup(urljoin(BASE, nxt), "article.product_pod")
pods2 = p2.select("article.product_pod")
print("next href:", nxt, "| status:", r2.status_code, "| books:", len(pods2), "| first:", pods2[0].select_one("h3 a")["title"])
time.sleep(1)

print("=== Halt path demo 1: random page returns 404 ===")
try:
    get_soup(BASE + "catalogue/no-such-book_9999/index.html", "div.product_main")
except SystemExit:
    print("halted as designed on 404")
time.sleep(1)

print("=== Halt path demo 2: 200 but marker missing ===")
try:
    get_soup(url_book, "article.product_pod")   # book page has no catalog pods
except SystemExit:
    print("halted as designed on missing marker")
