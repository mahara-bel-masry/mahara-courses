import pandas as pd, numpy as np
ages = pd.Series([25, np.nan, 31, 230, 28, 35])
print(ages.describe().round(2).to_dict())
bad = (ages < 0) | (ages > 100)
print(bad.sum(), ages[bad].tolist())
ages[bad] = np.nan
print(ages.median(), ages.isna().sum())
filled = ages.fillna(ages.median())
print(filled.tolist())
q1, q3 = ages.quantile([0.25, 0.75])
print(q1, q3, q3 - q1)
