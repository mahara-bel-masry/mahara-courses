import numpy as np
from scipy import stats
rng = np.random.default_rng(4)
old = rng.normal(10, 3, 40)
new = rng.normal(11.2, 3, 40)
d = new.mean() - old.mean()
se = (new.var(ddof=1) / 40 + old.var(ddof=1) / 40) ** 0.5
lo, hi = d - 2.0 * se, d + 2.0 * se
print("difference", round(d, 2))
print("standard error", round(se, 2))
print("rough interval", round(lo, 2), round(hi, 2))
sp = ((new.var(ddof=1) + old.var(ddof=1)) / 2) ** 0.5
print("effect size", round(d / sp, 2))
