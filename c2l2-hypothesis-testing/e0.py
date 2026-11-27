import numpy as np
from scipy import stats
rng = np.random.default_rng(41)
# invented story: checkout time in seconds, old flow vs new flow
n = 150
old = rng.normal(60, 15, n)
new = rng.normal(56, 15, n)
t, p = stats.ttest_ind(new, old, equal_var=False)
d = new.mean() - old.mean()
se = (new.var(ddof=1) / n + old.var(ddof=1) / n) ** 0.5
print("people per group", n)
print("difference", round(d, 2), "seconds")
print("p value", round(p, 4))
print("interval", round(d - 1.96 * se, 2), round(d + 1.96 * se, 2))
print("effect size", round(d / 15, 2))
