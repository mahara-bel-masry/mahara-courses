import numpy as np
from sklearn.preprocessing import StandardScaler
rng = np.random.default_rng(10)
x = rng.uniform(50, 200, 300).reshape(-1, 1)
train, test = x[:225], x[225:]
s = StandardScaler().fit(train)
print("train mean", round(float(s.mean_[0]), 1))
print("test mean after scaling", round(float(s.transform(test).mean()), 2))
print("train mean after scaling", round(float(s.transform(train).mean()), 2))
