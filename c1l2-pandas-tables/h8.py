import pandas as pd
df = pd.DataFrame({"x": [1, 2, 3]})
v = df[df["x"] > 1]
v["x"] = 0
print(df["x"].tolist())
d2 = df.copy()
d2.loc[d2["x"] > 1, "x"] = 0
print(d2["x"].tolist(), df["x"].tolist())
print(pd.Series(["1", "2"]).sum() , pd.Series(["1", "2"]).astype(int).sum())
