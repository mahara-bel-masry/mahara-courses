import numpy as np
from scipy import stats
rng = np.random.default_rng(11)
# no real difference at all, repeat the test many times
trials = 2000
hits = 0
for _ in range(trials):
    a = rng.normal(10, 3, 40)
    b = rng.normal(10, 3, 40)
    if stats.ttest_ind(a, b, equal_var=False)[1] < 0.05:
        hits += 1
print("tests run", trials)
print("false alarms at 0.05", hits, round(hits / trials, 3))
