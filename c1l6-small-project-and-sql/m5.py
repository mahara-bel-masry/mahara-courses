import pandas as pd, numpy as np
df = pd.read_csv("/tmp/shop_clean.csv")
df["ads_band"] = pd.cut(df["ads"], [-1, 15, 30, 50], labels=["low", "mid", "high"])
counts = df["ads_band"].value_counts()
print(counts.sort_index().to_dict())
t = df.pivot_table(index="branch", columns="ads_band", values="sales",
    aggfunc="mean", observed=True).round(1)
print(t)
print(df.sort_values("sales", ascending=False).head(3)[["branch", "ads",
    "visitors", "sales"]])
print("days with sales over 400:", int((df.sales > 400).sum()))
info = pd.DataFrame({"branch": ["Cairo", "Giza", "Aswan"], "staff": [8, 6, 5]})
mg = df.merge(info, on="branch")
sm = mg.groupby("staff")["sales"].mean()
ref = pd.Series([5, 6, 8], index=[5, 6, 8])
print(mg.shape, round(sm.corr(ref), 2))
