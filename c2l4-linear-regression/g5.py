import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
rng = np.random.default_rng(14)
n = 200
df = pd.DataFrame({"size": rng.normal(100, 20, n),
                   "city": rng.choice(["cairo", "giza", "fayoum"], n)})
bump = df["city"].map({"cairo": 40, "giza": 20, "fayoum": 0})
df["price"] = 30 + 2 * df["size"] + bump + rng.normal(0, 12, n)
res = smf.ols("price ~ size + C(city)", data=df).fit()
print(res.params.round(2))
print("R squared", round(res.rsquared, 3))
