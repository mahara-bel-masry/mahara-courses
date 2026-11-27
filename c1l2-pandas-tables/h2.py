import pandas as pd
df = pd.DataFrame({
    "item": ["phone", "case", "cable", "phone"],
    "qty": [2, 5, 10, 1],
    "price": [300.0, 20.0, 5.0, 300.0],
})
print(df)
print(df.shape, list(df.columns))
print(df.dtypes)
print(df.head(2))
