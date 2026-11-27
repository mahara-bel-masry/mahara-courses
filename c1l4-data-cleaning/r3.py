import pandas as pd
df = pd.DataFrame({"city": ["Cairo", "Giza", "Cairo", "Aswan"],
                   "level": ["low", "high", "mid", "low"],
                   "age": [25, 31, 28, 40]})
print(pd.get_dummies(df["city"]).astype(int).values.tolist())
order = {"low": 0, "mid": 1, "high": 2}
print(df["level"].map(order).tolist())
print(df["city"].astype("category").cat.codes.tolist())
print({c: str(t) for c, t in df.dtypes.items()})
num = df.select_dtypes("number").columns.tolist()
cat = df.select_dtypes("str").columns.tolist()
print(num, cat)
