import numpy as np
rng = np.random.default_rng(13)
# many unrelated columns, find the best looking pair
data = rng.normal(0, 1, (30, 40))
c = np.corrcoef(data.T)
np.fill_diagonal(c, 0)
print("columns", 40, "rows", 30)
print("pairs checked", 40 * 39 // 2)
print("strongest r by pure luck", round(np.abs(c).max(), 3))
