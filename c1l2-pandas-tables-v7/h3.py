import pandas as pd
df = pd.DataFrame({"item": ["phone", "case", "cable", "phone"],
    "qty": [2, 5, 10, 1], "price": [300.0, 20.0, 5.0, 300.0]})
print(df["qty"])
print(df[["item", "qty"]])
df["total"] = df["qty"] * df["price"]
print(df)
print(df.loc[1])
print(df.iloc[0, 1])
print(df.loc[df["total"] > 100, "item"])
