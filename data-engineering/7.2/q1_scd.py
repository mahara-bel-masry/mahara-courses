import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE cust(id INT, city TEXT, cur INT)")
db.execute("INSERT INTO cust VALUES (1, 'Cairo', 1)")
def move(cid, city):
    db.execute("UPDATE cust SET cur = 0 WHERE id = ?", (cid,))
    db.execute("INSERT INTO cust VALUES (?, ?, 1)", (cid, city))
move(1, "Giza")
print(db.execute("SELECT COUNT(*) FROM cust").fetchone())
print(db.execute("SELECT city FROM cust WHERE cur = 1").fetchone())
print(db.execute("SELECT city FROM cust WHERE cur = 0").fetchone())
