import pandas as pd
s = pd.Series(["10", "20", "x"])
print(pd.to_numeric(s, errors="coerce").tolist())
t = pd.Series([1, 2, 3, 4, 5, 6])
print(pd.cut(t, bins=[0, 2, 4, 6], labels=["low", "mid", "high"]).tolist())
print(t.rolling(3).mean().tolist())
print(t.cumsum().tolist(), t.diff().tolist())
print(t.sort_values(ascending=False).index.tolist())
