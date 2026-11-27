import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 8)
y = x ** 2
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y)
ax.set_ylim(0, 60)
ax.set_xticks([1, 4, 7])
ax.axhline(25, color="red")
ax.annotate("peak", (7, 49))
print(ax.get_ylim(), ax.get_xticks().tolist())
print(len(ax.lines), len(ax.texts))
for dpi in (50, 100):
    fig.savefig("t.png", dpi=dpi)
    import os; print(dpi, os.path.getsize("t.png") > 0)
os.remove("t.png")
plt.close(fig)
print(plt.get_fignums())
