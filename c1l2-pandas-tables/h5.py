import pandas as pd, numpy as np
df = pd.DataFrame({"age": [25, np.nan, 31, 40], "city": ["Cairo", "Giza", None, "Cairo"]})
print(df.isna().sum())
print(df.fillna({"age": df["age"].mean(), "city": "unknown"}))
print(df.dropna())
print(len(df.dropna()))
