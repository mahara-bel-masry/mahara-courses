import sqlite3
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.execute("""CREATE TABLE clients (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT)""")
db.execute("""CREATE TABLE tickets (
  id INTEGER PRIMARY KEY,
  client_id INTEGER NOT NULL REFERENCES clients(id),
  hours REAL)""")
db.execute("INSERT INTO clients VALUES (1, 'Clinic A', 'Cairo')")
db.execute("INSERT INTO tickets VALUES (1, 1, 2.5)")
print(db.execute("SELECT * FROM tickets").fetchall())
try:
    db.execute("INSERT INTO tickets VALUES (2, 99, 1.0)")
except sqlite3.IntegrityError as e:
    print("error:", e)
try:
    db.execute("INSERT INTO clients VALUES (2, NULL, 'Giza')")
except sqlite3.IntegrityError as e:
    print("error:", e)
print(db.execute("SELECT typeof(hours) FROM tickets").fetchall())
