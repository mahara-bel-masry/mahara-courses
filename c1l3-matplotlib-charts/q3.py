import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
names = ["A", "B", "C"]
vals = [1350, 650, 900]
fig, ax = plt.subplots()
bars = ax.bar(names, vals)
print(len(bars), [round(b.get_height()) for b in bars])
print(bars[0].get_x() < bars[1].get_x())
fig2, ax2 = plt.subplots()
ax2.barh(names, vals)
print(ax2.get_ylim())
