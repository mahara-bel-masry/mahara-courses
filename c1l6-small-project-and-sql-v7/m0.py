import pandas as pd, numpy as np, io
rng = np.random.default_rng(42)
n = 120
branch = rng.choice(["Cairo", "Giza", "Aswan"], n)
ad = rng.integers(0, 50, n)
visitors = rng.integers(80, 400, n)
sales = (visitors * 0.9 + ad * 2.5 + rng.normal(0, 25, n)).round(1)
df = pd.DataFrame({"branch": branch, "ads": ad, "visitors": visitors, "sales": sales})
# mess it up on purpose
df.loc[[3, 17, 40], "sales"] = np.nan
df.loc[[8], "ads"] = -5
df.loc[[22], "visitors"] = 9999
df.loc[[5, 6], "branch"] = ["cairo ", "GIZA"]
df.to_csv("/tmp/shop.csv", index=False)
raw = pd.read_csv("/tmp/shop.csv")
print(raw.shape)
print(raw.isna().sum().to_dict())
print(raw["branch"].value_counts().to_dict())
print(raw[["ads", "visitors", "sales"]].describe().loc[["min", "max"]].round(1))
