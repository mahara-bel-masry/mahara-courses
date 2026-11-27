import numpy as np
rng = np.random.default_rng(42)
a = rng.integers(1, 7, size=10)
print(a)
rng2 = np.random.default_rng(42)
print(rng2.integers(1, 7, size=10))
print(np.round(rng.normal(50, 10, size=5), 2))
print(np.array_equal(a, rng2.integers(1, 7, size=10)))
