import pandas as pd, numpy as np
df = pd.read_csv("/tmp/shop.csv")
df["branch"] = df["branch"].str.strip().str.title()
print(df["branch"].value_counts().to_dict())
df.loc[df["ads"] < 0, "ads"] = np.nan
df.loc[df["visitors"] > 1000, "visitors"] = np.nan
print("missing after fixes", df.isna().sum().to_dict())
for c in ["ads", "visitors", "sales"]:
    df[c + "_missing"] = df[c].isna().astype(int)
df = df.dropna(subset=["sales"])
print("rows after dropping rows with no sales", len(df))
for c in ["ads", "visitors"]:
    df[c] = df[c].fillna(df[c].median())
df.to_csv("/tmp/shop_clean.csv", index=False)
print(df.shape, df[["ads", "visitors", "sales"]].isna().sum().to_dict())
