import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]
fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig("line.png")
print(type(fig).__name__, type(ax).__name__)
print(fig.get_size_inches().tolist(), fig.dpi)
print(len(ax.lines), ax.lines[0].get_ydata().tolist())
