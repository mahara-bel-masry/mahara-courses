import pandas as pd
a = pd.DataFrame({"id": [1, 2, 3], "name": ["Ali", "Mona", "Sara"]})
b = pd.DataFrame({"id": [1, 2, 4], "score": [90, 80, 70]})
print(a.merge(b, on="id"))
print(a.merge(b, on="id", how="left"))
print(pd.concat([a, a]).shape)
print(a["name"].str.upper().tolist())
print(a["name"].str.len().tolist())
