import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
rng = np.random.default_rng(4)
a = rng.normal(0, 1, 40)
b = a + rng.normal(0, 0.05, 40)
y = 2 * a + rng.normal(0, 1, 40)
X = np.column_stack([a, b])
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.5, random_state=0)
for name, m in [("linear", LinearRegression()), ("ridge 1", Ridge(alpha=1.0)), ("ridge 10", Ridge(alpha=10.0))]:
    m.fit(Xtr, ytr)
    print(name, "coef", m.coef_.round(2), "test R2", round(m.score(Xte, yte), 3))
