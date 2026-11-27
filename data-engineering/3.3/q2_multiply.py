import sqlite3
db = sqlite3.connect("shop.db")
real = "SELECT SUM(total) FROM orders"
joined = """SELECT SUM(o.total) FROM orders o
JOIN items i ON i.order_id = o.id"""
safe = """SELECT SUM(total) FROM orders
WHERE id IN (SELECT order_id FROM items)"""
count = """SELECT o.id, COUNT(*) FROM orders o
JOIN items i ON i.order_id = o.id GROUP BY o.id"""
print(db.execute(real).fetchone())
print(db.execute(joined).fetchone())
print(db.execute(safe).fetchone())
print(db.execute(count).fetchall())
