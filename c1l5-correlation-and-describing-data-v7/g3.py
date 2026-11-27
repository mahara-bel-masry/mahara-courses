import pandas as pd, numpy as np
rng = np.random.default_rng(21)
n = 60
shop = rng.choice(["Cairo", "Giza", "Aswan"], n)
sales = rng.normal(100, 15, n).round(1)
sales[shop == "Giza"] += 20
df = pd.DataFrame({"shop": shop, "sales": sales})
print(df.shape)
print(df.groupby("shop")["sales"].agg(["count", "mean", "median", "std"]).round(1))
print("overall mean", round(df.sales.mean(), 1), "overall std", round(df.sales.std(), 1))
g = df.groupby("shop")["sales"].mean()
print("biggest gap between shops", round(g.max() - g.min(), 1))
print("share of total by shop", (df.groupby("shop")["sales"].sum() / df.sales.sum()).round(3).to_dict())
