import numpy as np
x = np.array([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
print(x.mean(), x.std(), x.var(), np.median(x))
z = (x - x.mean()) / x.std()
print(np.round(z, 2))
print(round(z.mean(), 10), z.std())
print(np.percentile(x, 50), np.percentile(x, 90))
