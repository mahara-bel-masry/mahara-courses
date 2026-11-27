import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
rng = np.random.default_rng(10)
size = rng.uniform(50, 200, 300)
age = rng.uniform(0, 40, 300)
price = 20 + 1.5 * size - 0.8 * age + rng.normal(0, 15, 300)
X = np.column_stack([size, age])
Xtr, Xte, ytr, yte = train_test_split(X, price, test_size=0.25, random_state=0)
base = DummyRegressor(strategy="mean").fit(Xtr, ytr)
lin = LinearRegression().fit(Xtr, ytr)
print("baseline MAE", round(mean_absolute_error(yte, base.predict(Xte)), 2))
print("linear MAE", round(mean_absolute_error(yte, lin.predict(Xte)), 2))
