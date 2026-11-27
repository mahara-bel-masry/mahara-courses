import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 7], label="A", marker="o")
ax.plot([1, 2, 3], [3, 3, 4], label="B", linestyle="--")
ax.set_title("sales")
ax.set_xlabel("day")
ax.set_ylabel("units")
ax.legend()
print(ax.get_title(), ax.get_xlabel(), ax.get_ylabel())
print([l.get_label() for l in ax.lines])
print(ax.get_xlim())
fig.savefig("two.png", dpi=100)
