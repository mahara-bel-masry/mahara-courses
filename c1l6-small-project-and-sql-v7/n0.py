import sqlite3, pandas as pd
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table branches "
    "(id integer primary key, name text, city text)")
cur.execute("create table sales (id integer primary key, "
    "branch_id integer, day text, amount real)")
cur.executemany("insert into branches values (?,?,?)", [(1, "Cairo",
    "Cairo"), (2, "Giza", "Giza"), (3, "Aswan", "Aswan")])
rows = [(1, 1, "2026-01-01", 120.5), (2, 1, "2026-01-02", 98.0), (3, 2,
    "2026-01-01", 150.0),
        (4, 2, "2026-01-02", 170.5), (5, 3, "2026-01-01", 80.0), (6, 3,
            "2026-01-03", 95.5), (7, 2, "2026-01-03", 160.0)]
cur.executemany("insert into sales values (?,?,?,?)", rows)
con.commit()
print(cur.execute(
    "select count(*) from sales").fetchone())
print(cur.execute(
    "select * from sales limit 3").fetchall())
print(cur.execute(
    "select name from branches order by name").fetchall())
con.close()
