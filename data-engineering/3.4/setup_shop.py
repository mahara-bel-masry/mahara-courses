import sqlite3
db = sqlite3.connect("shop.db")
db.executescript("""
DROP TABLE IF EXISTS orders;
CREATE TABLE orders(id INTEGER PRIMARY KEY, customer TEXT, total INTEGER);
INSERT INTO orders VALUES (1,'Ali',300),(2,'Ali',100),(3,'Mona',200),(4,'Omar',50);
""")
db.commit()
