import numpy as np
rng = np.random.default_rng(5)
x = rng.normal(100, 15, 200000)
m, s = x.mean(), x.std()
print("mean", round(m, 2), "std", round(s, 2))
for k in (1, 2, 3):
    print("within", k, "std", round(((x > m - k * s) & (x < m + k * s)).mean(), 4))
print("share above 130", round((x > 130).mean(), 4))
z = (130 - 100) / 15
print("z for 130", z)
means = rng.exponential(10, (20000, 30)).mean(axis=1)
print("exp data mean", 10, "means of 30 mean", round(means.mean(), 2), "std", round(means.std(), 2), "expected", round(10 / 30**0.5, 2))
