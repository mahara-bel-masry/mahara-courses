import numpy as np
rng = np.random.default_rng(8)
# a curve: strong relation, weak correlation
x = rng.uniform(-3, 3, 400)
y = x ** 2 + rng.normal(0, 0.3, 400)
print("pearson r for a clear curve", round(np.corrcoef(x, y)[0, 1], 3))
# one outlier changes everything
a = rng.normal(0, 1, 30)
b = rng.normal(0, 1, 30)
print("r without outlier", round(np.corrcoef(a, b)[0, 1], 3))
a2 = np.append(a, 12)
b2 = np.append(b, 12)
print("r with one outlier", round(np.corrcoef(a2, b2)[0, 1], 3))
