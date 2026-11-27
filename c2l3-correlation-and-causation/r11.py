import numpy as np
rng = np.random.default_rng(15)
# invented: two groups, inside each group y goes DOWN with x
gx, gy = [], []
for g in range(3):
    x = rng.normal(2 + 3 * g, 0.7, 100)
    y = 10 + 6 * g - 1.5 * (x - (2 + 3 * g)) + rng.normal(0, 0.8, 100)
    print("group", g, "r inside", round(np.corrcoef(x, y)[0, 1], 2))
    gx += list(x)
    gy += list(y)
print("r with all groups mixed", round(np.corrcoef(gx, gy)[0, 1], 2))
