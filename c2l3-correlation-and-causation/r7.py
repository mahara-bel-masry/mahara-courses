import numpy as np
rng = np.random.default_rng(6)
# two independent random walks, like two invented price charts
big = 0
for _ in range(1000):
    a = rng.normal(0, 1, 250).cumsum()
    b = rng.normal(0, 1, 250).cumsum()
    if abs(np.corrcoef(a, b)[0, 1]) > 0.5:
        big += 1
print("pairs with r above 0.5 or below minus 0.5", big, "of 1000")
da, db = np.diff(a), np.diff(b)
print("last pair r on levels", round(np.corrcoef(a, b)[0, 1], 3))
print("last pair r on daily changes", round(np.corrcoef(da, db)[0, 1], 3))
