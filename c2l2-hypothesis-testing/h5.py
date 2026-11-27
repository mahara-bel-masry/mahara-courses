import numpy as np
from scipy import stats
rng = np.random.default_rng(19)
# huge sample, tiny difference
a = rng.normal(10.00, 3, 200000)
b = rng.normal(10.05, 3, 200000)
t, p = stats.ttest_ind(b, a, equal_var=False)
print("difference", round(b.mean() - a.mean(), 3), "minutes")
print("p value", p)
d = (b.mean() - a.mean()) / 3
print("effect size about", round(d, 3), "standard deviations")
