import pandas as pd, numpy as np
rng = np.random.default_rng(7)
n = 12
hours = np.array([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9])
score = np.array([52, 55, 50, 61, 66, 63, 70, 74, 72, 80, 83, 88])
df = pd.DataFrame({"hours": hours, "score": score})
print(df.head(4))
print(df.describe().round(2))
print("mean hours", round(df.hours.mean(), 2), "mean score", round(df.score.mean(), 2))
