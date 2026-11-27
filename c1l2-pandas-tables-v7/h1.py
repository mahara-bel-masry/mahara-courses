import pandas as pd
s = pd.Series([120, 80, 45], index=["sat", "sun", "mon"])
print(s)
print(s["sun"], s.iloc[0], s.dtype)
print(s * 2)
print(s[s > 50])
print(s.mean(), s.sum())
