from bs4 import BeautifulSoup
html = """<html><body>
<div class='item'><h2>Pen</h2><span class='price'>25</span></div>
<div class='item'><h2>Book</h2><span class='price'>90</span></div>
</body></html>"""
soup = BeautifulSoup(html, "html.parser")
print(soup.h2.text)
items = soup.select("div.item")
print(len(items))
for it in items:
    name = it.select_one("h2").text
    price = int(it.select_one(".price").text)
    print(name, price)
