import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({"branch": ["A", "B", "C"], "sales": [1350, 650, 900]})
ax = df.plot(x="branch", y="sales", kind="bar", legend=False)
print(type(ax).__name__, len(ax.patches))
g = df.sort_values("sales", ascending=False)
print(g["branch"].tolist())
ax2 = g.plot.barh(x="branch", y="sales")
ax2.set_title("sales by branch")
print(ax2.get_title())
fig = ax.get_figure()
fig.savefig("p.png", dpi=50)
import os
print(os.path.getsize("p.png") > 500); os.remove("p.png")
