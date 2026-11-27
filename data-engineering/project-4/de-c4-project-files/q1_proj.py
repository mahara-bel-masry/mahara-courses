import sqlite3
pages = {"p1": [("Pen", 25), ("Book", 90)], "p2": [("Pen", 25), ("Bag", 60)]}
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE items(name TEXT UNIQUE, price INTEGER)")
for rows in pages.values():
    db.executemany("INSERT OR IGNORE INTO items VALUES (?, ?)", rows)
print(db.execute("SELECT COUNT(*) FROM items").fetchone())
print(db.execute("SELECT name FROM items ORDER BY price DESC LIMIT 1").fetchone())
print(db.execute("SELECT SUM(price) FROM items").fetchone())
