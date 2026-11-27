import numpy as np
rng = np.random.default_rng(34)
# same story, but now assign the drug by coin flip
severity = rng.uniform(0, 10, 2000)
drug = rng.random(2000) < 0.5
recovery = 80 - 5 * severity + 3 * drug + rng.normal(0, 4, 2000)
print("average recovery with drug", round(recovery[drug].mean(), 1))
print("average recovery without drug", round(recovery[~drug].mean(), 1))
print("difference", round(recovery[drug].mean() - recovery[~drug].mean(), 2))
print("average severity with drug", round(severity[drug].mean(), 2))
print("average severity without drug", round(severity[~drug].mean(), 2))
