# solutions.py
# DE Course 4 - Lesson 1 - executed solutions for the 5 exercises
# Target: books.toscrape.com (a site built for scraping practice)
# Needs: requests, beautifulsoup4  ->  pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"

def get_soup(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    # The server sends content-type: text/html with no charset, and requests
    # guesses ISO-8859-1. The page declares UTF-8 in its meta tag, so set it.
    r.encoding = "utf-8"
    return BeautifulSoup(r.text, "html.parser"), r

print("=== Exercise 1: check the status code before parsing ===")
url_book = BASE + "catalogue/a-light-in-the-attic_1000/index.html"
r = requests.get(url_book, timeout=30)
print("GET book page ->", r.status_code)
if r.status_code == 200:
    print("200 means success, safe to parse")
else:
    print("not 200, do not parse this body")

print()
print("=== Exercise 2: data from a book detail page ===")
soup, _ = get_soup(url_book)
title = soup.select_one("div.product_main h1").get_text(strip=True)
price = soup.select_one("div.product_main p.price_color").get_text(strip=True)
avail = soup.select_one("div.product_main p.instock.availability").get_text(strip=True)
upc = soup.select_one("table.table.table-striped td").get_text(strip=True)
print("title:", title)
print("price:", price)
print("availability:", avail)
print("UPC:", upc)

print()
print("=== Exercise 3: star rating from the home page ===")
home, _ = get_soup(BASE)
second = home.select("article.product_pod")[1]
rating_class = [c for c in second.select_one("p.star-rating")["class"] if c != "star-rating"][0]
second_title = second.select_one("h3 a")["title"]
print("second book:", second_title, "| rating:", rating_class)

print()
print("=== Exercise 4: all category names ===")
cats = home.select("ul.nav-list ul li a")
print("category count:", len(cats))
print("first 5:", [c.get_text(strip=True) for c in cats[:5]])
print("last 5:", [c.get_text(strip=True) for c in cats[-5:]])

print()
print("=== Exercise 5: follow the next button and count books on page 2 ===")
nxt = home.select_one("li.next a")["href"]
page2, r2 = get_soup(BASE + nxt)
print("followed:", nxt, "| status:", r2.status_code)
pods2 = page2.select("article.product_pod")
print("books on page 2:", len(pods2))
print("first book on page 2:", pods2[0].select_one("h3 a")["title"])
