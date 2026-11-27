import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(3)
# invented shops: ad spend (thousands) and weekly sales (thousands)
ad = rng.uniform(1, 10, 80)
sales = 20 + 3 * ad + rng.normal(0, 4, 80)
X = sm.add_constant(ad)
res = sm.OLS(sales, X).fit()
print("intercept", round(res.params[0], 2), "slope", round(res.params[1], 2))
print("slope std error", round(res.bse[1], 3))
lo, hi = res.conf_int()[1]
print("slope interval", round(lo, 2), round(hi, 2))
print("slope p value", res.pvalues[1])
print("R squared", round(res.rsquared, 3))
