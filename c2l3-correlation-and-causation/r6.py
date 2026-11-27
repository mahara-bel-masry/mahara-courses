import numpy as np
from scipy import stats
rng = np.random.default_rng(2)
# a curve that always goes up, but not in a straight line
x = rng.uniform(0, 5, 200)
y = np.exp(x) + rng.normal(0, 1, 200)
print("pearson", round(stats.pearsonr(x, y)[0], 3))
print("spearman", round(stats.spearmanr(x, y)[0], 3))
# the outlier again, now with ranks
a = rng.normal(0, 1, 30)
b = rng.normal(0, 1, 30)
a2, b2 = np.append(a, 12), np.append(b, 12)
print("pearson with outlier", round(stats.pearsonr(a2, b2)[0], 3))
print("spearman with outlier", round(stats.spearmanr(a2, b2)[0], 3))
