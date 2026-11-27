import numpy as np
rng = np.random.default_rng(21)
# invented: sicker patients get the drug, so the drug looks harmful
severity = rng.uniform(0, 10, 2000)
drug = rng.random(2000) < severity / 10
recovery = 80 - 5 * severity + 3 * drug + rng.normal(0, 4, 2000)
print("average recovery with drug", round(recovery[drug].mean(), 1))
print("average recovery without drug", round(recovery[~drug].mean(), 1))
mild = severity < 3
print("mild cases with drug", round(recovery[drug & mild].mean(), 1))
print("mild cases without drug", round(recovery[~drug & mild].mean(), 1))
