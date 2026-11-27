import numpy as np
c = np.array([1, 2, 2, 3, 3, 3])
v, n = np.unique(c, return_counts=True)
print(v, n)
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate([a, b]))
print(np.vstack([a, b]))
print(np.hstack([a, b]))
