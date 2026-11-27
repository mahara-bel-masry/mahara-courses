import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE flat(order_id INT, client TEXT, city TEXT, item TEXT);
INSERT INTO flat VALUES (1,'Ali','Cairo','pen'),(2,'Ali','Cairo','book'),
 (3,'Mona','Giza','pen');
CREATE TABLE clients(id INTEGER PRIMARY KEY, name TEXT, city TEXT);
INSERT INTO clients(name, city) SELECT DISTINCT client, city FROM flat;
""")
print(db.execute("SELECT COUNT(*) FROM flat").fetchone())
print(db.execute("SELECT COUNT(*) FROM clients").fetchone())
db.execute("UPDATE clients SET city = 'Alex' WHERE name = 'Ali'")
print(db.execute("SELECT name, city FROM clients ORDER BY id").fetchall())
