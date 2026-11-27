import numpy as np
from scipy import stats
rng = np.random.default_rng(31)
# invented story: same 25 people typed a text before and after a short training
before = rng.normal(40, 8, 25)
after = before + rng.normal(2.0, 3.0, 25)
t1, p1 = stats.ttest_ind(after, before, equal_var=False)
t2, p2 = stats.ttest_rel(after, before)
print("mean change", round((after - before).mean(), 2))
print("two groups test p value", round(p1, 4))
print("paired test p value", round(p2, 4))
