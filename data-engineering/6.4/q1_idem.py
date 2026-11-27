import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE done(day TEXT PRIMARY KEY)")
db.execute("CREATE TABLE sales(day TEXT, total INTEGER)")
def run(day, total):
    if db.execute("SELECT 1 FROM done WHERE day = ?", (day,)).fetchone():
        return "skip"
    db.execute("INSERT INTO sales VALUES (?, ?)", (day, total))
    db.execute("INSERT INTO done VALUES (?)", (day,))
    return "ok"
print(run("mon", 100), run("mon", 100))
print(db.execute("SELECT COUNT(*) FROM sales").fetchone())
