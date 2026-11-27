import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(8)
n = 120
size = rng.normal(100, 20, n)
rooms = size / 25 + rng.normal(0, 0.3, n)
price = 50 + 2 * size + 5 * rooms + rng.normal(0, 15, n)
print("r between size and rooms", round(np.corrcoef(size, rooms)[0, 1], 3))
a = sm.OLS(price, sm.add_constant(size)).fit()
b = sm.OLS(price, sm.add_constant(np.column_stack([size, rooms]))).fit()
print("size slope alone", round(a.params[1], 2), "std error", round(a.bse[1], 3))
print("size slope with rooms", round(b.params[1], 2), "std error", round(b.bse[1], 3))
print("rooms slope", round(b.params[2], 2), "std error", round(b.bse[2], 3))
