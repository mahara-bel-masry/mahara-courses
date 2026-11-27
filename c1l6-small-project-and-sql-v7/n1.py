import sqlite3, pandas as pd
exec(open("n0.py").read().split("print(")[0])
q = ("select branch_id, count(*) as n, "
     "sum(amount) as total, "
     "round(avg(amount),1) as mean from sales "
     "group by branch_id order by total desc")
print(pd.read_sql(q, con))
print(pd.read_sql("select * from sales "
    "where amount > 100 and day >= '2026-01-02'", con))
