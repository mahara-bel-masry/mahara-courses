import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng(2)
x = rng.uniform(0, 10, 50)
y = 2 * x + rng.normal(0, 2, 50)
fig, axs = plt.subplots(1, 2, figsize=(8, 3))
axs[0].scatter(x, y)
axs[1].boxplot([x, y])
print(axs.shape, fig.get_size_inches().tolist())
print(round(np.corrcoef(x, y)[0, 1], 3))
fig.tight_layout()
fig.savefig("pair.png")
import os; print(os.path.getsize("pair.png") > 1000)
for f in ("line.png","two.png","pair.png"):
    if os.path.exists(f): os.remove(f)
