import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
w = 0.35
a = [30, 45, 38]
b = [25, 50, 42]
x = np.arange(3)
fig, ax = plt.subplots()
r1 = ax.bar(x - w / 2, a, w, label="2025")
r2 = ax.bar(x + w / 2, b, w, label="2026")
print(len(ax.patches), [p.get_height() for p in r2])
m = np.array([[1.0, 0.8, 0.1], [0.8, 1.0, 0.3], [0.1, 0.3, 1.0]])
fig2, ax2 = plt.subplots()
im = ax2.imshow(m, cmap="viridis", vmin=0, vmax=1)
fig2.colorbar(im)
print(im.get_array().shape, im.get_clim())
fig3, ax3 = plt.subplots()
ax3.plot([1, 10, 100, 1000], [1, 2, 3, 4])
ax3.set_xscale("log")
print(ax3.get_xscale())
fig4, ax4 = plt.subplots()
wedges, texts = ax4.pie([50, 30, 20], labels=["x", "y", "z"])
print(len(wedges), round(wedges[0].theta2 - wedges[0].theta1, 1))
fig5, axs = plt.subplots(2, 2, sharex=True, sharey=True)
print(axs.shape, axs[0, 0].get_shared_x_axes().joined(axs[0, 0], axs[1, 1]))
