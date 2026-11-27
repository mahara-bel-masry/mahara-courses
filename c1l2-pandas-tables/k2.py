import pandas as pd
df = pd.DataFrame({"id": [1, 2, 2, 3], "v": [10, 20, 20, 30]})
print(df.duplicated().tolist())
print(df.drop_duplicates().shape)
print(df["v"].nunique(), df["id"].is_unique)
d = pd.to_datetime(pd.Series(["2026-01-05", "2026-02-10"]))
print(d.dt.month.tolist(), d.dt.day_name().tolist())
print((d[1] - d[0]).days)
