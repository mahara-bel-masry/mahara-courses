import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL);
CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INT, product_id INT,
                    qty INT, month TEXT);
INSERT INTO customers VALUES (1,'Ali'),(2,'Mona'),(3,'Omar');
INSERT INTO products VALUES (1,'pen',2.0),(2,'book',10.0);
INSERT INTO orders VALUES (1,1,1,5,'2026-01'),(2,1,2,1,'2026-02'),
 (3,2,2,3,'2026-02');
""")
q1 = """SELECT p.name, SUM(o.qty) FROM orders o
JOIN products p ON p.id = o.product_id
GROUP BY p.name ORDER BY 2 DESC"""
q2 = """SELECT o.month, SUM(o.qty * p.price) FROM orders o
JOIN products p ON p.id = o.product_id GROUP BY o.month"""
q3 = """SELECT c.name FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL"""
for q in (q1, q2, q3):
    print(sorted(db.execute(q).fetchall(), key=str))
