import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
rng = np.random.default_rng(5)
days = pd.date_range("2026-03-01", periods=30)
base = 100 + np.arange(30) * 2
sales = base + rng.normal(0, 8, 30)
df = pd.DataFrame({"day": days, "sales": sales.round(1)})
df["avg7"] = df["sales"].rolling(7).mean().round(1)
print(df.shape, df["sales"].min(), df["sales"].max())
print(df["avg7"].isna().sum(), df["avg7"].iloc[-1])
fig, axs = plt.subplots(1, 3, figsize=(12, 3))
axs[0].plot(df["day"], df["sales"], label="daily")
axs[0].plot(df["day"], df["avg7"], label="avg7")
axs[0].legend()
axs[1].hist(df["sales"], bins=6)
axs[2].boxplot(df["sales"])
print([len(a.lines) for a in axs], len(axs[1].patches))
print(round(df["sales"].mean(), 1), round(df["sales"].median(), 1))
q1, q3 = np.percentile(df["sales"], [25, 75])
print(round(q1, 1), round(q3, 1))
w = (df["sales"] > q3 + 1.5 * (q3 - q1)).sum()
print(int(w))
