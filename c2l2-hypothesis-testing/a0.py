import numpy as np
from statsmodels.stats.proportion import proportions_ztest
rng = np.random.default_rng(5)
# invented story: old button vs new button, did the visitor buy
n = 2000
buy_a = rng.random(n) < 0.10
buy_b = rng.random(n) < 0.125
ca, cb = int(buy_a.sum()), int(buy_b.sum())
print("old buyers", ca, "of", n, round(ca / n, 4))
print("new buyers", cb, "of", n, round(cb / n, 4))
z, p = proportions_ztest([cb, ca], [n, n])
print("z", round(z, 3), "p value", round(p, 4))
