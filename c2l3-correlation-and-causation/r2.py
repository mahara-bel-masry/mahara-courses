import numpy as np
rng = np.random.default_rng(5)
# invented: hot weather drives both ice cream sales and swimming accidents
temp = rng.normal(30, 5, 365)
ice = 20 * temp + rng.normal(0, 60, 365)
swim = 0.5 * temp + rng.normal(0, 3, 365)
print("r ice cream vs accidents", round(np.corrcoef(ice, swim)[0, 1], 3))
# remove the part explained by temperature from both
def resid(v):
    s, i = np.polyfit(temp, v, 1)
    return v - (s * temp + i)
print("r after removing temperature", round(np.corrcoef(resid(ice), resid(swim))[0, 1], 3))
