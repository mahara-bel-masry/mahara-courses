import sqlite3
rows = [("Pen", 25), ("Book", 90)]
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE items(name TEXT UNIQUE, price INTEGER)")
db.executemany("INSERT OR IGNORE INTO items VALUES (?, ?)", rows)
db.executemany("INSERT OR IGNORE INTO items VALUES (?, ?)", rows)
print(db.execute("SELECT COUNT(*) FROM items").fetchone())
print(db.execute("SELECT name, price FROM items ORDER BY price").fetchall())
print(db.execute("SELECT SUM(price) FROM items").fetchone())
