import numpy as np
rng = np.random.default_rng(6)
for n in (5, 30, 120, 480):
    means = rng.exponential(10, (20000, n)).mean(axis=1)
    print("n", n, "std of means", round(means.std(), 3), "10/sqrt(n)", round(10 / n**0.5, 3))
n = 30
means = rng.exponential(10, (20000, n)).mean(axis=1)
counts, edges = np.histogram(means, bins=7)
print("bin counts of sample means", counts.tolist())
print("skew sign of raw data:", "right" if rng.exponential(10, 100000).mean() > np.median(rng.exponential(10, 100000)) else "left")
print("mean vs median of the sample means", round(means.mean(), 2), round(np.median(means), 2))
