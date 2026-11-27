import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
rng = np.random.default_rng(2)
x = rng.uniform(0, 10, 30).reshape(-1, 1)
y = 3 * x.ravel() + rng.normal(0, 4, 30)
xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.6, random_state=1)
for deg in [1, 3, 7]:
    m = make_pipeline(PolynomialFeatures(deg), StandardScaler(), LinearRegression())
    m.fit(xtr, ytr)
    print("degree", deg, "train R2", round(m.score(xtr, ytr), 2), "test R2", round(m.score(xte, yte), 2))
