import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
y = np.array([100, 120, 140, 160, 180, 200])
good = y + np.array([5, -5, 5, -5, 5, -5])
bad = good.copy()
bad[0] = bad[0] + 60
for name, p in [("steady errors", good), ("one big miss", bad)]:
    print(name, "MAE", round(mean_absolute_error(y, p), 2), "RMSE", round(mean_squared_error(y, p) ** 0.5, 2))
