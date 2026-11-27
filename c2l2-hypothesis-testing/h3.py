import numpy as np
from scipy import stats
rng = np.random.default_rng(13)
# real difference of 1.2 minutes, different sample sizes
for n in (10, 40, 160, 640):
    trials = 1000
    hits = 0
    for _ in range(trials):
        a = rng.normal(10.0, 3, n)
        b = rng.normal(11.2, 3, n)
        if stats.ttest_ind(b, a, equal_var=False)[1] < 0.05:
            hits += 1
    print("n per group", n, "detected", round(hits / trials, 3))
