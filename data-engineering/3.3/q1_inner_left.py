import sqlite3
db = sqlite3.connect("shop.db")
inner = """SELECT c.name, o.total FROM customers c
JOIN orders o ON o.customer_id = c.id"""
left = """SELECT c.name, o.total FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id"""
anti = left.replace("c.name, o.total", "c.name") + " WHERE o.id IS NULL"
print(db.execute(inner).fetchall())
print(db.execute(left).fetchall())
print(db.execute(anti).fetchall())
