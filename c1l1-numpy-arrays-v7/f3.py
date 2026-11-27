import numpy as np
rng = np.random.default_rng(7)
sales = rng.integers(20, 100, size=(4, 5))
print(sales)
print(sales.sum(axis=1))
print(sales.mean(axis=0))
print(sales.max(), sales.argmax())
print(np.unravel_index(sales.argmax(), sales.shape))
print(sales.mean(), (sales > sales.mean()).sum())
