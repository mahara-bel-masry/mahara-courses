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
print(df.shape)
print({c: str(t) for c, t in df.dtypes.items()})
print(df.isna().sum().to_dict())
print(df["city"].unique().tolist())
print(df.duplicated().sum())
