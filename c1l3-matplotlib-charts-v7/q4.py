import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng(1)
d = rng.normal(50, 10, 1000)
fig, ax = plt.subplots()
counts, edges, _ = ax.hist(d, bins=10)
print(int(counts.sum()), len(edges))
print(round(d.mean(), 2), round(d.std(), 2))
print(counts.astype(int).tolist())
