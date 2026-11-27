import sqlite3
db = sqlite3.connect("shop.db")
db.executescript("""
DROP TABLE IF EXISTS customers; DROP TABLE IF EXISTS orders; DROP TABLE IF EXISTS items;
CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER, total INTEGER);
CREATE TABLE items(order_id INTEGER, sku TEXT);
INSERT INTO customers VALUES (1,'Ali'),(2,'Mona'),(3,'Omar');
INSERT INTO orders VALUES (10,1,300),(11,1,100),(12,2,200);
INSERT INTO items VALUES (10,'A'),(10,'B'),(10,'C'),(11,'A'),(12,'B');
""")
db.commit()
