import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("/tmp/shop_clean.csv")
X = pd.get_dummies(df[["branch", "ads", "visitors"]], columns=["branch"], dtype=int)
y = df["sales"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
print("train", len(Xtr), "test", len(Xte))
m = LinearRegression().fit(Xtr, ytr)
print("coef ads", round(m.coef_[0], 2), "coef visitors", round(m.coef_[1], 2))
print("MAE train", round(mean_absolute_error(ytr, m.predict(Xtr)), 2))
print("MAE test", round(mean_absolute_error(yte, m.predict(Xte)), 2))
base = np.full(len(yte), ytr.mean())
print("MAE baseline (always the mean)", round(mean_absolute_error(yte,
    base), 2))
print("R squared test", round(m.score(Xte, yte), 3))
