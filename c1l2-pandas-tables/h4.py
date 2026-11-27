import pandas as pd
df = pd.DataFrame({"item": ["phone", "case", "cable", "phone"],
    "qty": [2, 5, 10, 1], "price": [300.0, 20.0, 5.0, 300.0]})
df["total"] = df["qty"] * df["price"]
print(df.describe())
print(df["item"].value_counts())
print(df.groupby("item")["total"].sum())
print(df.sort_values("total", ascending=False).head(2))
