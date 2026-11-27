import numpy as np
rng = np.random.default_rng(2)
n = 200000
d = rng.integers(1, 7, size=(n, 2))
total = d.sum(axis=1)
a = d[:, 0] == 6
b = total >= 10
print("P(first is 6)", round(a.mean(), 4))
print("P(sum >= 10)", round(b.mean(), 4))
print("P(sum >= 10 | first is 6)", round((a & b).sum() / a.sum(), 4))
print("exact 1/2 =", 0.5, " exact 6/36 =", round(6 / 36, 4))
print("P(A and B)", round((a & b).mean(), 4), "P(A) * P(B)", round(a.mean() * b.mean(), 4))
