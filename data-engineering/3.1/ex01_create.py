import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript(open("schema.sql").read())
rows = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name").fetchall()
print(rows)
print(conn.execute("PRAGMA table_info(orders)").fetchall()[2])
