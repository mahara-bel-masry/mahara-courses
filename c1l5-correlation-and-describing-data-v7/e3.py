import numpy as np
rng = np.random.default_rng(3)
months = np.arange(1, 13)
ice = 10 + 4 * months + rng.normal(0, 3, 12)
drown = 5 + 2 * months + rng.normal(0, 2, 12)
print("r ice cream vs drowning (invented)", round(np.corrcoef(ice, drown)[0, 1], 3))
print("both depend on month")
for _ in range(3):
    p = rng.normal(0, 1, 12); q = rng.normal(0, 1, 12)
    print("r of two random lists", round(np.corrcoef(p, q)[0, 1], 3))
