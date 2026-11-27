import numpy as np
rng = np.random.default_rng(21)
# same drug story as before: sicker patients get the drug more often
severity = rng.uniform(0, 10, 2000)
drug = rng.random(2000) < severity / 10
recovery = 80 - 5 * severity + 3 * drug + rng.normal(0, 4, 2000)
ones = np.ones(2000)
naive = np.column_stack([ones, drug])
adjusted = np.column_stack([ones, drug, severity])
b1 = np.linalg.lstsq(naive, recovery, rcond=None)[0]
b2 = np.linalg.lstsq(adjusted, recovery, rcond=None)[0]
print("drug effect without severity", round(b1[1], 2))
print("drug effect with severity", round(b2[1], 2))
print("severity effect", round(b2[2], 2))
