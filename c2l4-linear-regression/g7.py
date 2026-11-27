import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(31)
x = rng.uniform(1, 10, 50)
y = 10 + 2 * x + rng.normal(0, 2, 50)
a = sm.OLS(y, sm.add_constant(x)).fit()
x2, y2 = np.append(x, 30), np.append(y, 10)
b = sm.OLS(y2, sm.add_constant(x2)).fit()
print("slope without the odd shop", round(a.params[1], 2))
print("slope with one odd shop", round(b.params[1], 2))
print("R squared without", round(a.rsquared, 3), "with", round(b.rsquared, 3))
