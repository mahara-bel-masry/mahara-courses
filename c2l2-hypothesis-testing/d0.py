import numpy as np
from scipy import stats
rng = np.random.default_rng(4)
old = rng.normal(10, 3, 40)
new = rng.normal(11.2, 3, 40)
two = stats.ttest_ind(new, old, equal_var=False, alternative="two-sided")[1]
one = stats.ttest_ind(new, old, equal_var=False, alternative="greater")[1]
worse = stats.ttest_ind(new, old, equal_var=False, alternative="less")[1]
print("two sided p", round(two, 4))
print("one sided greater p", round(one, 4))
print("one sided less p", round(worse, 4))
