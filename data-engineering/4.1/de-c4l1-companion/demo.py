# demo.py
# DE Course 4 - Lesson 1 - demo executed in the video
# Target: books.toscrape.com (a site built for scraping practice)
# Needs: requests, beautifulsoup4  ->  pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

print("=== 1) GET request ===")
r = requests.get(URL, timeout=30)
print("status_code:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print("content-length header:", r.headers.get("content-length"))
print("actual bytes:", len(r.content))
print("first 60 chars of body:", repr(r.text[:60]))

print()
print("=== 2) status codes ===")
r404 = requests.get(URL + "page-not-there-xyz.html", timeout=30)
print("GET /page-not-there-xyz.html ->", r404.status_code)
rhead = requests.head(URL, timeout=30)
print("HEAD / ->", rhead.status_code, "| body bytes:", len(rhead.content))

print()
print("=== 3) encoding trap and its fix ===")
# The content-type header has no charset, so requests guesses ISO-8859-1.
print("default guess r.encoding:", r.encoding)
soup_wrong = BeautifulSoup(r.text, "html.parser")
price_wrong = soup_wrong.select_one("p.price_color").get_text(strip=True)
print("price with wrong encoding:", price_wrong)
print("guess from content r.apparent_encoding:", r.apparent_encoding)
r.encoding = "utf-8"  # the page declares UTF-8 in its meta tag
soup = BeautifulSoup(r.text, "html.parser")
price = soup.select_one("p.price_color").get_text(strip=True)
print("price after fix:", price)

print()
print("=== 4) one book card from the real page ===")
pod = soup.select_one("article.product_pod")
print(pod.prettify()[:700])

print()
print("=== 5) CSS selectors executed ===")
pods = soup.select("article.product_pod")
print("article.product_pod ->", len(pods), "books on the page")
h3s = soup.select("h3")
print("h3 alone ->", len(h3s), "headings on the page")
promo = soup.select("#promotions")
print("#promotions ->", len(promo), "element |", promo[0].name if promo else None)
prices = soup.select("p.price_color")
print("p.price_color ->", len(prices), "| first price:", prices[0].get_text(strip=True))
titles = soup.select("article.product_pod h3 a")
print("article.product_pod h3 a ->", len(titles), "| first title:", titles[0]["title"])
stock = soup.select_one("p.instock.availability")
print("p.instock.availability ->", stock.get_text(strip=True))
rating = soup.select_one("p.star-rating")
print("p.star-rating -> class list:", rating["class"])
cats = soup.select("ul.nav-list ul li a")
print("ul.nav-list ul li a ->", len(cats), "categories | first:", cats[0].get_text(strip=True))
nxt = soup.select_one("li.next a")
print("li.next a -> href:", nxt["href"], "| text:", nxt.get_text(strip=True))
imgs = soup.select("img[alt]")
print("img[alt] ->", len(imgs), "| first alt:", imgs[0]["alt"])

print()
print("=== 6) raw HTML vs what the browser renders ===")
scripts = soup.select("script")
print("script tags on the page:", len(scripts))
# Note: a naive r.text.count("<script") gives 9. The two extra hits are not real
# script elements: one sits inside an IE conditional comment (html5shim), and one
# is a string literal inside another script (the jQuery fallback document.write).
print("all the content is already in the original HTML (no JavaScript needed)")
