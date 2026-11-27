import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(23)
# many useless columns: R squared always rises, adjusted does not
n = 60
y = rng.normal(0, 1, n)
for k in (1, 5, 20, 40):
    X = sm.add_constant(rng.normal(0, 1, (n, k)))
    r = sm.OLS(y, X).fit()
    print("useless columns", k, "R squared", round(r.rsquared, 3), "adjusted", round(r.rsquared_adj, 3))
