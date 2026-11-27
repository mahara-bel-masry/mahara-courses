import numpy as np
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.sum(), m.sum(axis=0), m.sum(axis=1))
print(m.mean(axis=0), m.max(axis=1))
print(m + 10)
print(m * np.array([1, 10, 100]))
col = np.array([[1], [2]])
print(m + col)
try:
    print(m + np.array([1, 2]))
except ValueError as e:
    print("ValueError")
