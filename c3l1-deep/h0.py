import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
rng = np.random.default_rng(10)
size = rng.uniform(50, 200, 300)
age = rng.uniform(0, 40, 300)
price = 20 + 1.5 * size - 0.8 * age + rng.normal(0, 15, 300)
X = np.column_stack([size, age])
Xtr, Xte, ytr, yte = train_test_split(X, price, test_size=0.25, random_state=0)
print("train rows", len(Xtr), "test rows", len(Xte))
m = LinearRegression().fit(Xtr, ytr)
print("coef", m.coef_.round(2), "intercept", round(m.intercept_, 2))
p = m.predict(Xte)
print("MAE", round(mean_absolute_error(yte, p), 2))
print("RMSE", round(mean_squared_error(yte, p) ** 0.5, 2))
print("R2", round(r2_score(yte, p), 3))
