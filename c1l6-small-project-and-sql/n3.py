import sqlite3
exec(open("n0.py").read().split("print(")[0])
name = "Giza'; drop table sales; --"
try:
    cur.executescript("select * from branches "
        "where name = '" + name + "'")
except Exception as e:
    pass
T = "select name from sqlite_master where type='table'"
print("tables after unsafe string:", [r[0] for r in cur.execute(T)])
print(cur.execute("select count(*) from branches "
    "where name = ?", (name,)).fetchone())
print("tables after safe query:", [r[0] for r in cur.execute(T)])
