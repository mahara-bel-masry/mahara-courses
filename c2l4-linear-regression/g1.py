import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(3)
ad = rng.uniform(1, 10, 80)
sales = 20 + 3 * ad + rng.normal(0, 4, 80)
res = sm.OLS(sales, sm.add_constant(ad)).fit()
resid = res.resid
print("residual mean", round(resid.mean(), 6))
print("residual std", round(resid.std(ddof=2), 2))
print("noise std I used", 4)
low = resid[ad < 5.5]
high = resid[ad >= 5.5]
print("spread for small ad", round(low.std(), 2), "large ad", round(high.std(), 2))
