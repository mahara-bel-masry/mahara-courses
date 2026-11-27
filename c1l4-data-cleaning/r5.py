import pandas as pd, numpy as np, io
raw = """id,name,city,age,salary,joined,gender
1, Ali ,Cairo,25,5000,2024-01-15,M
2,mona,cairo,,6200,2024-02-20,F
3,Sara,Giza,31,abc,2024-03-05,F
4,Omar,Cairo,230,7000,2024-13-40,M
5,Hana,Giza,28,5500,2024-04-10,f
5,Hana,Giza,28,5500,2024-04-10,f
6,Youssef,,35,,2024-05-01,M
"""
def clean(df):
    log = {}
    n0 = len(df)
    df = df.drop_duplicates().copy()
    log["dups"] = n0 - len(df)
    for c in ("name", "city"):
        df[c] = df[c].str.strip().str.title()
    df["gender"] = df["gender"].str.upper()
    before = df["salary"].isna().sum()
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    log["salary_bad"] = int(df["salary"].isna().sum() - before)
    df["joined"] = pd.to_datetime(df["joined"], errors="coerce")
    log["date_bad"] = int(df["joined"].isna().sum())
    bad = (df["age"] < 0) | (df["age"] > 100)
    log["age_bad"] = int(bad.sum())
    df.loc[bad, "age"] = np.nan
    log["na_before_fill"] = df.isna().sum().to_dict()
    df["age"] = df["age"].fillna(df["age"].median())
    df["salary"] = df["salary"].fillna(df["salary"].median())
    df["city"] = df["city"].fillna("Unknown")
    return df, log
df, log = clean(pd.read_csv(io.StringIO(raw)))
print(log)
print(df[["name", "city", "age", "salary"]].to_string(index=False))
print(df.isna().sum().to_dict())
print(round(df["salary"].mean(), 1), df["salary"].median())
print(df.groupby("city")["salary"].mean().round(1).to_dict())
