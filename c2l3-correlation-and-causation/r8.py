import numpy as np
import pandas as pd
rng = np.random.default_rng(12)
# invented students: four columns, one hidden cause
n = 300
sleep = rng.normal(7, 1, n)
hours = rng.normal(5, 2, n)
phone = rng.normal(4, 1.5, n) - 0.5 * (sleep - 7)
score = 40 + 5 * hours + 4 * sleep + rng.normal(0, 8, n)
df = pd.DataFrame({"hours": hours, "sleep": sleep,
                   "phone": phone, "score": score})
print(df.corr().round(2))
print("rows", len(df))
