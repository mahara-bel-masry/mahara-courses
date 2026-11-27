import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(5)
# noise grows with x: a broken assumption
x = rng.uniform(1, 10, 300)
y = 5 + 2 * x + rng.normal(0, 0.5 * x, 300)
res = sm.OLS(y, sm.add_constant(x)).fit()
r = res.resid
print("spread for x below 5.5", round(r[x < 5.5].std(), 2))
print("spread for x above 5.5", round(r[x >= 5.5].std(), 2))
robust = sm.OLS(y, sm.add_constant(x)).fit(cov_type="HC3")
print("slope std error normal", round(res.bse[1], 3))
print("slope std error robust", round(robust.bse[1], 3))
