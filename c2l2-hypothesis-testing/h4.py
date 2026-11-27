import numpy as np
from scipy import stats
rng = np.random.default_rng(17)
# twenty useless ideas, all tested against the same old page
old = rng.normal(10, 3, 40)
small = []
for i in range(20):
    new = rng.normal(10, 3, 40)
    small.append(stats.ttest_ind(new, old, equal_var=False)[1])
small = np.array(small)
print("smallest p value", round(small.min(), 4))
print("ideas under 0.05", int((small < 0.05).sum()), "of 20")
print("chance of at least one by luck", round(1 - 0.95 ** 20, 3))
print("bonferroni line", 0.05 / 20)
