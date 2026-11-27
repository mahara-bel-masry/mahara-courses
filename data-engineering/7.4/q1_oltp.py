import sqlite3
db = sqlite3.connect(":memory:")
T = "CREATE TABLE orders(id INTEGER PRIMARY KEY, city TEXT, total INT)"
db.execute(T)
ROWS = [(1, "Cairo", 10), (2, "Giza", 20), (3, "Cairo", 30)]
db.executemany("INSERT INTO orders VALUES (?, ?, ?)", ROWS)
print(db.execute("SELECT * FROM orders WHERE id = 2").fetchone())
Q = "SELECT city, SUM(total) FROM orders GROUP BY city ORDER BY city"
print(db.execute(Q).fetchall())
