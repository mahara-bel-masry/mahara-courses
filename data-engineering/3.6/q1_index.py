import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE logs(id INTEGER PRIMARY KEY, user_id INTEGER, msg TEXT)")
db.executemany("INSERT INTO logs(user_id, msg) VALUES (?, 'x')",
               [(i % 5000,) for i in range(200000)])
q = "SELECT COUNT(*) FROM logs WHERE user_id = 4321"
plan = "EXPLAIN QUERY PLAN " + q
print(db.execute(plan).fetchall()[0][3])
print(db.execute(q).fetchone())
db.execute("CREATE INDEX idx_user ON logs(user_id)")
print(db.execute(plan).fetchall()[0][3])
print(db.execute(q).fetchone())
