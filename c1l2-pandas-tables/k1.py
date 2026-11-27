import pandas as pd
df = pd.DataFrame({"item": ["phone", "case", "cable", "phone"],
    "qty": [2, 5, 10, 1], "price": [300.0, 20.0, 5.0, 300.0]})
df["total"] = df["qty"] * df["price"]
print(df.groupby("item").agg(n=("qty", "sum"), avg=("total", "mean")))
print(df.rename(columns={"qty": "count"}).columns.tolist())
print(df.drop(columns=["price"]).shape)
print(df["price"].map(lambda p: p * 2).tolist())
print(df["item"].map({"phone": "mobile"}).tolist())
