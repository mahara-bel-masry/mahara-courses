import pandas as pd, numpy as np
x = np.arange(1, 11)
y = np.exp(x / 2)
df = pd.DataFrame({"x": x, "y": y})
print("pearson", round(df.x.corr(df.y), 3))
print("spearman", round(df.x.corr(df.y, method="spearman"), 3))
print("ranks of y", df.y.rank().astype(int).tolist())
df["group"] = ["a", "b"] * 5
print(df.groupby("group")["y"].mean().round(1).to_dict())
passed = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 1])
hours = np.array([1, 2, 3, 3, 4, 5, 5, 6, 7, 8])
print("hours vs passed (0 or 1)", round(np.corrcoef(hours, passed)[0, 1], 3))
print("mean hours failed", hours[passed == 0].mean(), "passed", round(hours[passed == 1].mean(), 2))
