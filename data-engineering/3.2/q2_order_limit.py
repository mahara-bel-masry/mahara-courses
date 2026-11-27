from setup_store import make

conn = make()
sql = "SELECT product, qty * price AS revenue FROM sales ORDER BY revenue DESC LIMIT 3"
print(conn.execute(sql).fetchall())
