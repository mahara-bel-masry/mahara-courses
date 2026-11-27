import pandas as pd
df = pd.DataFrame({"item": ["phone", "case", "cable", "phone"],
    "qty": [2, 5, 10, 1], "price": [300.0, 20.0, 5.0, 300.0]})
print(df.set_index("item").loc["case"].tolist())
print(df.query("qty > 1 and price < 100"))
print(df.nlargest(2, "qty")[["item", "qty"]])
print(df.apply(lambda r: r["qty"] * r["price"], axis=1).tolist())
print(df["qty"].to_numpy(), type(df["qty"].to_numpy()).__name__)
print(df["price"].between(10, 100).tolist())
print(df["item"].isin(["case", "cable"]).sum())
print(df.loc[df["item"] == "phone", "qty"].sum())
print(df.sample(2, random_state=1).index.tolist())
print(df.reset_index(drop=True).equals(df))
