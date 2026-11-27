import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("/tmp/shop_clean.csv")
X = pd.get_dummies(df[["branch", "ads", "visitors"]], columns=["branch"], dtype=int)
y = df["sales"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
m = LinearRegression().fit(Xtr, ytr)
err = (yte - m.predict(Xte))
r = pd.DataFrame({"branch": df.loc[yte.index, "branch"],
    "actual": yte.round(1),
    "pred": m.predict(Xte).round(1), "miss": err.round(1)})
order = r.miss.abs().sort_values(ascending=False).index
print(r.reindex(order).head(3).to_string())
print("mean miss", round(err.mean(), 2), "worst", round(err.abs().max(), 1))
by = r.assign(a=r.miss.abs()).groupby("branch")["a"]
print("avg abs miss by branch", by.mean().round(1).to_dict())
