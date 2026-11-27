import sqlite3, pandas as pd
exec(open("n0.py").read().split("print(")[0])
q = ("select b.name, count(*) as n, "
     "sum(s.amount) as total "
     "from sales s join branches b on b.id = s.branch_id "
     "group by b.name order by total desc")
sql = pd.read_sql(q, con)
print(sql)
df = pd.read_sql("select * from sales",
    con).merge(pd.read_sql("select * from branches", con),
    left_on="branch_id", right_on="id", suffixes=("", "_b"))
pd_ = df.groupby("name")["amount"].agg(["count", "sum"]).sort_values("sum", ascending=False)
print(pd_)
a = sql.set_index("name")["total"].round(1).to_dict()
b = pd_["sum"].round(1).to_dict()
print("same totals:", a == b)
print("left join keeps branches with no sales:")
cur.execute("insert into branches "
    "values (4, 'Luxor', 'Luxor')")
print(pd.read_sql("select b.name, count(s.id) as n "
    "from branches b left join sales s "
    "on s.branch_id = b.id group by b.name", con))
print("plain join, Luxor is gone:")
print(pd.read_sql("select b.name, count(*) as n "
    "from branches b join sales s "
    "on s.branch_id = b.id group by b.name", con))
