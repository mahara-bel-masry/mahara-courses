import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
rng = np.random.default_rng(10)
size = rng.uniform(50, 200, 300)
age = rng.uniform(0, 40, 300)
noise = rng.normal(0, 15, 300)
price = 20 + 1.5 * size - 0.8 * age + noise
tiny = rng.normal(0, 0.001, 300)
leak = price / 1000 + tiny
honest = np.column_stack([size, age])
leaky = np.column_stack([size, age, leak])
for name, X in [("honest", honest), ("with leak", leaky)]:
    Xtr, Xte, ytr, yte = train_test_split(
        X, price, test_size=0.25, random_state=0)
    m = LinearRegression().fit(Xtr, ytr)
    print(name, "test R2", round(m.score(Xte, yte), 3))
