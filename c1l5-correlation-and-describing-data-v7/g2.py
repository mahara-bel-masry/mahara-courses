import numpy as np
rng = np.random.default_rng(5)
sym = rng.normal(50, 10, 1000)
skew = rng.exponential(10, 1000)
for name, v in (("symmetric", sym), ("right skewed", skew)):
    counts, edges = np.histogram(v, bins=5)
    print(name, "mean", round(v.mean(), 1), "median", round(np.median(v), 1))
    print("  bin counts", counts.tolist())
print("mean is bigger than median in skewed:", skew.mean() > np.median(skew))
