import numpy as np
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
rng = np.random.default_rng(8)
X = rng.normal(0, 1, (120, 30))
y = 3 * X[:, 0] - 2 * X[:, 1] + rng.normal(0, 2, 120)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
pipe = make_pipeline(StandardScaler(), Ridge())
gs = GridSearchCV(pipe, {"ridge__alpha": [0.1, 1, 10, 100]}, cv=5, scoring="r2")
gs.fit(Xtr, ytr)
print("best alpha", gs.best_params_["ridge__alpha"])
print("cv R2", round(gs.best_score_, 3))
print("test R2", round(gs.score(Xte, yte), 3))
