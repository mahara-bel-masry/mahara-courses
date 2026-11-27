import numpy as np, pandas as pd
rng = np.random.default_rng(3)
n = 12
df = pd.DataFrame({
    "branch": rng.choice(["A", "B", "C"], size=n),
    "units": rng.integers(1, 20, size=n),
    "price": rng.choice([10.0, 25.0, 40.0], size=n),
})
df.loc[[2, 7], "units"] = np.nan
print(df)
print(df.isna().sum().to_dict())
df["units"] = df["units"].fillna(df["units"].median())
df["revenue"] = df["units"] * df["price"]
print(df.groupby("branch")["revenue"].agg(["sum", "count"]))
top = df.sort_values("revenue", ascending=False).head(3)
print(top[["branch", "revenue"]])
print(round(df["revenue"].mean(), 2), df["revenue"].median())
print((df["revenue"] > df["revenue"].mean()).sum())
