import csv, io, sqlite3
RAW = "name,price\nPen, 25\nBook,90\nBag,\n"
rows = list(csv.DictReader(io.StringIO(RAW)))
clean = [(r["name"], int(r["price"])) for r in rows if r["price"].strip()]
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE items(name TEXT, price INTEGER)")
db.executemany("INSERT INTO items VALUES (?, ?)", clean)
print(len(rows), len(clean))
print(db.execute("SELECT COUNT(*) FROM items").fetchone())
print(db.execute("SELECT SUM(price) FROM items").fetchone())
