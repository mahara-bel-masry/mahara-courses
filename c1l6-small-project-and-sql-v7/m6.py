import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("/tmp/shop_clean.csv")
X = pd.get_dummies(df[["branch", "ads", "visitors"]], columns=["branch"], dtype=int)
y = df["sales"]
for rs in (0, 0, 1, 2, 3):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=rs)
    m = LinearRegression().fit(Xtr, ytr)
    print("random_state", rs, "test MAE", round(mean_absolute_error(yte,
        m.predict(Xte)), 2))
