import numpy as np
x = np.arange(-5, 6)
y = x ** 2
print("x", x.tolist())
print("y", y.tolist())
print("r for y = x squared", round(np.corrcoef(x, y)[0, 1], 4))
x2 = np.arange(1, 12)
print("r for y = x squared, x positive", round(np.corrcoef(x2, x2 ** 2)[0, 1], 4))
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 60])
print("r clean", round(np.corrcoef(a, a)[0, 1], 4))
print("r with one outlier", round(np.corrcoef(a, b)[0, 1], 4))
print("r without it", round(np.corrcoef(a[:-1], b[:-1])[0, 1], 4))
