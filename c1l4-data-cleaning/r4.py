import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
df = pd.DataFrame({"x": np.arange(20), "y": [0] * 10 + [1] * 10})
tr, te = train_test_split(df, test_size=0.25, random_state=0)
print(len(tr), len(te), sorted(set(tr.index) & set(te.index)))
tr2, te2 = train_test_split(df, test_size=0.25, random_state=0,
                            stratify=df["y"])
print("stratified test", te2["y"].value_counts().to_dict(),
      "plain test", te["y"].value_counts().to_dict())
m = tr["x"].mean(); s = tr["x"].std()
print(round(m, 2), round(s, 2), round(((te["x"] - m) / s).mean(), 3))
