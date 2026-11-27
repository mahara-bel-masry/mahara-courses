import numpy as np
from scipy import stats
rng = np.random.default_rng(4)
old = rng.normal(10.0, 3.0, 40)
new = rng.normal(11.2, 3.0, 40)
t, p = stats.ttest_ind(new, old, equal_var=False)
print("t statistic", round(t, 3))
print("p value", round(p, 4))
