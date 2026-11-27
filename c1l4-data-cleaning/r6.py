import pandas as pd, numpy as np, io
from sklearn.model_selection import train_test_split
raw = """id,city,age,salary,level,bought
1,Cairo,25,5000,low,0
2,cairo,,6200,mid,1
3,Giza,31,abc,high,1
4,Cairo,230,7000,mid,0
5,Giza,28,5500,low,0
6,Aswan,35,,high,1
7,Giza,40,8000,high,1
8,Cairo,22,4800,low,0
9,aswan,33,6100,mid,1
10,Cairo,29,5300,low,0
"""
df = pd.read_csv(io.StringIO(raw))
bad = df.isna().any(axis=1) | pd.to_numeric(df.salary, errors="coerce").isna()
print("rows with any NaN or text-number:", int(bad.sum()), "of", len(df))
print("dropna rows left:", len(df.dropna()))
kept = df.dropna()
print("after dropna, abc row id:", kept.loc[kept.salary == "abc", "id"].tolist(),
      "age 230 row id:", kept.loc[kept.age == 230, "id"].tolist())
df["city"] = df["city"].str.strip().str.title()
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df.loc[(df.age < 0) | (df.age > 100), "age"] = np.nan
df["age_missing"] = df["age"].isna().astype(int)
df["salary_missing"] = df["salary"].isna().astype(int)
train, test = train_test_split(df, test_size=0.3, random_state=1,
                               stratify=df["bought"])
print("train", len(train), "test", len(test))
am, sm = train["age"].median(), train["salary"].median()
print("train medians", am, sm)
for d in (train, test):
    d["age"] = d["age"].fillna(am); d["salary"] = d["salary"].fillna(sm)
mp = {"low": 0, "mid": 1, "high": 2}
X = pd.concat([train, test])
X["level"] = X["level"].map(mp)
X = pd.get_dummies(X, columns=["city"], dtype=int)
mu, sd = X.loc[train.index, "salary"].mean(), X.loc[train.index, "salary"].std()
X["salary_z"] = (X["salary"] - mu) / sd
Xtr, Xte = X.loc[train.index], X.loc[test.index]
print("columns", list(X.columns))
print("train salary mean", round(mu, 1), "std", round(sd, 1))
print("train z mean", round(Xtr.salary_z.mean(), 3),
      "test z mean", round(Xte.salary_z.mean(), 3))
print("bought train", Xtr.bought.value_counts().to_dict(),
      "test", Xte.bought.value_counts().to_dict())
print(Xtr.shape, Xte.shape)
