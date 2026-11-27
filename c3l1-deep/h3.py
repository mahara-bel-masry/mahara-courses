import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
rng = np.random.default_rng(10)
size = rng.uniform(50, 200, 300)
age = rng.uniform(0, 40, 300)
price = 20 + 1.5 * size - 0.8 * age + rng.normal(0, 15, 300)
X = np.column_stack([size, age])
Xtr, Xte, ytr, yte = train_test_split(X, price, test_size=0.25, random_state=0)
pipe = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
pipe.fit(Xtr, ytr)
print("steps", list(pipe.named_steps))
print("scaled coef", pipe[-1].coef_.round(2))
print("scaler means", pipe[0].mean_.round(1))
print("test R2", round(pipe.score(Xte, yte), 3))
