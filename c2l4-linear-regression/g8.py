import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(37)
# invented: income grows by percent with years of experience
years = rng.uniform(0, 20, 200)
income = 8000 * np.exp(0.06 * years + rng.normal(0, 0.15, 200))
raw = sm.OLS(income, sm.add_constant(years)).fit()
logged = sm.OLS(np.log(income), sm.add_constant(years)).fit()
print("R squared on raw income", round(raw.rsquared, 3))
print("R squared on log income", round(logged.rsquared, 3))
print("log slope", round(logged.params[1], 4))
print("percent per year", round((np.exp(logged.params[1]) - 1) * 100, 2))
