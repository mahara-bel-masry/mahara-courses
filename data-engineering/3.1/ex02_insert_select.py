import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript(open("schema.sql").read())
conn.execute("INSERT INTO customers VALUES (1, 'منى', 'Cairo')")
conn.execute("INSERT INTO customers VALUES (2, 'Ali', 'Giza')")
conn.execute("INSERT INTO orders VALUES (10, 1, 448.5)")
conn.execute("INSERT INTO orders VALUES (11, 1, 150.5)")
conn.execute("INSERT INTO orders VALUES (12, 2, 75.25)")
print(conn.execute("SELECT * FROM customers").fetchall())
print(conn.execute("SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id").fetchall())
