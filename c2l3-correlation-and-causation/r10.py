import numpy as np
from scipy import stats
rng = np.random.default_rng(9)
# same weak link between x and y, three sample sizes
for n in (20, 200, 2000):
    x = rng.normal(0, 1, n)
    y = 0.25 * x + rng.normal(0, 1, n)
    r, p = stats.pearsonr(x, y)
    z = np.arctanh(r)
    se = 1 / (n - 3) ** 0.5
    lo, hi = np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)
    print("n", n, "r", round(r, 2), "p", round(p, 4),
          "interval", round(lo, 2), round(hi, 2))
