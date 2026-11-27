import numpy as np
from sklearn.model_selection import (train_test_split,
    cross_val_score, KFold)
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (mean_absolute_error,
    mean_squared_error, r2_score)
rng = np.random.default_rng(21)
size = rng.uniform(40, 180, 300)
age = rng.uniform(0, 30, 300)
price = 15 + 2.0 * size - 1.2 * age + rng.normal(0, 12, 300)
X = np.column_stack([size, age])
Xtr, Xte, ytr, yte = train_test_split(X, price,
    test_size=0.25, random_state=0)
base = DummyRegressor().fit(Xtr, ytr)
print("baseline MAE", round(mean_absolute_error(
    yte, base.predict(Xte)), 2))
models = {"linear": LinearRegression(),
    "ridge": make_pipeline(StandardScaler(), Ridge(alpha=1.0))}
cv = KFold(n_splits=5, shuffle=True, random_state=0)
for name, m in models.items():
    m.fit(Xtr, ytr)
    p = m.predict(Xte)
    print(name, "MAE", round(mean_absolute_error(yte, p), 2),
        "RMSE", round(mean_squared_error(yte, p) ** 0.5, 2),
        "R2", round(r2_score(yte, p), 3))
    s = cross_val_score(m, Xtr, ytr, cv=cv, scoring="r2")
    print(name, "cv R2", round(s.mean(), 3))
leak = price / 1000 + rng.normal(0, 0.001, 300)
XL = np.column_stack([X, leak])
Xtr, Xte, ytr, yte = train_test_split(XL, price,
    test_size=0.25, random_state=0)
m = LinearRegression().fit(Xtr, ytr)
print("with leak test R2", round(m.score(Xte, yte), 3))
