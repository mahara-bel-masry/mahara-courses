import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("/tmp/shop_clean.csv")
X = pd.get_dummies(df[["branch", "ads", "visitors"]], columns=["branch"], dtype=int)
y = df["sales"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
m = LinearRegression().fit(Xtr, ytr)
print("clean: coef visitors", round(m.coef_[1], 2), "MAE test", round(mean_absolute_error(yte, m.predict(Xte)), 2))
bad = Xtr.copy()
bad.iloc[0, 1] = 9000
mb = LinearRegression().fit(bad, ytr)
print("one typo, visitors 9000: coef visitors", round(mb.coef_[1], 2), "MAE test", round(mean_absolute_error(yte, mb.predict(Xte)), 2))
