from setup_store import make

conn = make()
sql = "SELECT city, COUNT(*), SUM(qty * price) FROM sales GROUP BY city ORDER BY city"
print(conn.execute(sql).fetchall())
sql = "SELECT product, SUM(qty) FROM sales GROUP BY product HAVING SUM(qty) > 3 ORDER BY product"
print(conn.execute(sql).fetchall())
