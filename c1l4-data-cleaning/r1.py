import pandas as pd, io
raw = """id,name,city,age,salary,joined,gender
1, Ali ,Cairo,25,5000,2024-01-15,M
2,mona,cairo,,6200,2024-02-20,F
3,Sara,Giza,31,abc,2024-03-05,F
4,Omar,Cairo,230,7000,2024-13-40,M
5,Hana,Giza,28,5500,2024-04-10,f
5,Hana,Giza,28,5500,2024-04-10,f
6,Youssef,,35,,2024-05-01,M
"""
df = pd.read_csv(io.StringIO(raw))
df = df.drop_duplicates()
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()
df["gender"] = df["gender"].str.upper()
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["joined"] = pd.to_datetime(df["joined"], errors="coerce")
print(df.shape)
print(df["city"].value_counts(dropna=False).to_dict())
print(df["gender"].value_counts().to_dict())
print(df["salary"].tolist())
print(df["joined"].isna().sum())
