import sqlite3
db = sqlite3.connect("shop.db")
avg = "SELECT AVG(total) FROM orders"
above = """SELECT id, total FROM orders
WHERE total > (SELECT AVG(total) FROM orders)"""
print(db.execute(avg).fetchone())
print(db.execute(above).fetchall())
