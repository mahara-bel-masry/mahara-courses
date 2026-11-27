import numpy as np
import statsmodels.api as sm
rng = np.random.default_rng(3)
ad = rng.uniform(1, 10, 80)
sales = 20 + 3 * ad + rng.normal(0, 4, 80)
res = sm.OLS(sales, sm.add_constant(ad)).fit()
new = np.array([[1.0, 6.0]])
pred = res.get_prediction(new).summary_frame(alpha=0.05)
print("predicted mean sales at ad 6", round(pred["mean"][0], 2))
print("interval for the average shop", round(pred["mean_ci_lower"][0], 2), round(pred["mean_ci_upper"][0], 2))
print("interval for one new shop", round(pred["obs_ci_lower"][0], 2), round(pred["obs_ci_upper"][0], 2))
