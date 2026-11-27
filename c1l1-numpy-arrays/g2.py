import numpy as np
x = np.array([10.0, np.nan, 30.0])
print(x.sum(), np.nansum(x), np.nanmean(x))
print(np.isnan(x))
print(x[~np.isnan(x)])
print(np.nan == np.nan)
