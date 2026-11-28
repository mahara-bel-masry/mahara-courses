import sqlite3, sys
try:
    import duckdb
except ImportError:
    duckdb=None
print("python", sys.version.split()[0], "sqlite", sqlite3.sqlite_version, "duckdb", duckdb.__version__ if duckdb else "not installed in this python")
def run(name, con, q):
    try:
        r = con.execute(q).fetchall(); print(f"[R] {name}: {r}")
    except Exception as e:
        print(f"[ERR] {name}: {type(e).__name__}: {e}")
s = sqlite3.connect(":memory:")
for q in ["create table a(id int, v text)","create table b(id int, w text)","insert into a values (1,'x'),(2,'y')","insert into b values (2,'p'),(3,'q')"]: s.execute(q)
d = duckdb.connect(":memory:") if duckdb else None
for q in ([] if d is None else ["create table a(id int, v text)","create table b(id int, w text)","insert into a values (1,'x'),(2,'y')","insert into b values (2,'p'),(3,'q')"]): d.execute(q)
tests = {
 "window ROW_NUMBER": "select id, row_number() over (order by id desc) from a",
 "LAG": "select id, lag(id) over (order by id) from a",
 "CTE": "with c as (select id from a) select count(*) from c",
 "recursive CTE": "with recursive n(i) as (select 1 union all select i+1 from n where i<5) select sum(i) from n",
 "LEFT JOIN": "select a.id, b.w from a left join b on a.id=b.id order by 1",
 "RIGHT JOIN": "select a.id, b.w from a right join b on a.id=b.id order by 2",
 "FULL JOIN": "select a.id, b.id from a full join b on a.id=b.id order by 1,2",
 "EXCEPT": "select id from a except select id from b",
 "date": "select date('2026-11-27','start of month')",
}
for k,q in tests.items():
    print("--",k); run("sqlite", s, q)
    if d is None: continue
    q2 = "select date_trunc('month', date '2026-11-27')" if k=="date" else q
    run("duckdb", d, q2)
