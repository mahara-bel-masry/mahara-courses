import pandas as pd, numpy as np
rng = np.random.default_rng(11)
n = 40
size = rng.integers(40, 160, n)
rooms = (size // 35 + rng.integers(0, 2, n))
age = rng.integers(1, 30, n)
price = (size * 20 + rooms * 50 - age * 10 + rng.normal(0, 60, n)).round()
df = pd.DataFrame({"size": size, "rooms": rooms, "age": age, "price": price})
print(df.shape)
print(df.corr().round(2))
print(df.corr()["price"].drop("price").sort_values(ascending=False).round(2))
print("spearman size-price", round(df["size"].corr(df["price"], method="spearman"), 3))
print(df.groupby("rooms")["price"].mean().round(0).to_dict())
