from setup_store import make

conn = make()
print(conn.execute("SELECT product, qty FROM sales").fetchall()[:2])
print(conn.execute("SELECT product FROM sales WHERE city = 'Cairo' AND qty > 3").fetchall())
print(conn.execute("SELECT DISTINCT city FROM sales ORDER BY city").fetchall())
