import pandas as pd

df = pd.read_csv("data/customers.csv")
print(df.shape)
df["email"] = df["email"].str.strip().str.lower()
df["name"] = df["name"].str.strip().str.title()
print(df["email"].tolist())
df["city"] = df["city"].fillna("Unknown")
df["signup"] = pd.to_datetime(df["signup"], errors="coerce")
print(df["signup"].isna().sum())
df = df.drop_duplicates(subset="email")
print(df.shape)
print(df[["email", "city"]].to_dict("records")[0])
