import numpy as np
from scipy import stats
rng = np.random.default_rng(7)
true_mean = 50
hit = 0; widths = []
trials = 2000
for _ in range(trials):
    s = rng.normal(true_mean, 12, 25)
    se = s.std(ddof=1) / 25**0.5
    t = stats.t.ppf(0.975, 24)
    lo, hi = s.mean() - t * se, s.mean() + t * se
    hit += lo <= true_mean <= hi
    widths.append(hi - lo)
print("t multiplier for 24 df", round(stats.t.ppf(0.975, 24), 3), "z multiplier", round(stats.norm.ppf(0.975), 3))
print("t multiplier for 999 df", round(stats.t.ppf(0.975, 999), 3))
print("share of intervals that contain the true mean", round(hit / trials, 3))
print("average width", round(np.mean(widths), 2))
s = rng.normal(true_mean, 12, 25)
print("one sample mean", round(s.mean(), 2))
print("scipy interval", [round(float(x), 2) for x in stats.t.interval(0.95, 24, loc=s.mean(), scale=stats.sem(s))])
