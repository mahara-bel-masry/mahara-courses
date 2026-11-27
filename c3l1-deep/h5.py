import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
rng = np.random.default_rng(10)
size = rng.uniform(50, 200, 300)
age = rng.uniform(0, 40, 300)
price = 20 + 1.5 * size - 0.8 * age + rng.normal(0, 15, 300)
X = np.column_stack([size, age])
cv = KFold(n_splits=5, shuffle=True, random_state=0)
s = cross_val_score(LinearRegression(), X, price, cv=cv, scoring="r2")
print("fold R2", s.round(3))
print("mean", round(s.mean(), 3), "std", round(s.std(), 3))
