import pandas as pd, numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
def make(seed, n=60):
    rng = np.random.default_rng(seed)
    names = ["Cairo", "Giza", "Aswan"]
    d = pd.DataFrame({"branch": rng.choice(names, n),
        "ads": rng.integers(0, 50, n),
        "visitors": rng.integers(80, 400, n)})
    noise = rng.normal(0, 25, n)
    d["sales"] = (d.visitors * 0.9 + d.ads * 2.5 + noise).round(1)
    return d
def prep(d):
    d = d.copy()
    d["branch"] = d["branch"].str.strip().str.title()
    d.loc[d["ads"] < 0, "ads"] = np.nan
    d.loc[d["visitors"] > 1000, "visitors"] = np.nan
    return d
def feats(d, cols=None):
    X = pd.get_dummies(d[["branch", "ads", "visitors"]], columns=["branch"], dtype=int)
    if cols is None: return X
    return X.reindex(columns=cols, fill_value=0)
train = prep(pd.read_csv("/tmp/shop_clean.csv"))
Xtr = feats(train)
m = LinearRegression().fit(Xtr, train["sales"])
new = prep(make(99))
print("new batch rows", len(new))
print("MAE on a new batch", round(mean_absolute_error(new["sales"],
    m.predict(feats(new, Xtr.columns))), 2))
new2 = prep(make(7, 5)); new2["branch"] = "Cairo"
print("one-branch batch columns before align", list(feats(new2).columns))
print("after align", list(feats(new2, Xtr.columns).columns))
print("columns kept in same order", list(Xtr.columns))
