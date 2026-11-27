import sqlite3
db = sqlite3.connect("shop.db")
q = """WITH per_customer AS (
  SELECT customer, SUM(total) AS spent
  FROM orders GROUP BY customer
)
SELECT customer, spent FROM per_customer
WHERE spent > 200 ORDER BY spent DESC"""
print(db.execute(q).fetchall())
