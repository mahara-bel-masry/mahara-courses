import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE items(id INTEGER PRIMARY KEY, price INTEGER)")
SQL = ("INSERT INTO items VALUES (?, ?) "
       "ON CONFLICT(id) DO UPDATE "
       "SET price = excluded.price")
db.executemany(SQL, [(1, 25), (2, 90)])
db.executemany(SQL, [(2, 95), (3, 40)])
print(db.execute("SELECT COUNT(*) FROM items").fetchone())
print(db.execute("SELECT price FROM items WHERE id = 2").fetchone())
