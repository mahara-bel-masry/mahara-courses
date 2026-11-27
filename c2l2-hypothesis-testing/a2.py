import numpy as np
from scipy import stats
rng = np.random.default_rng(23)
# no real difference, but we peek ten times and stop at the first p under 0.05
runs = 1000
stopped = 0
final = 0
for _ in range(runs):
    a = rng.normal(10, 3, 400)
    b = rng.normal(10, 3, 400)
    hit = False
    for k in range(40, 401, 40):
        if stats.ttest_ind(a[:k], b[:k], equal_var=False)[1] < 0.05:
            hit = True
    stopped += hit
    final += stats.ttest_ind(a, b, equal_var=False)[1] < 0.05
print("peeked ten times, false alarms", round(stopped / runs, 3))
print("looked once at the end, false alarms", round(final / runs, 3))
