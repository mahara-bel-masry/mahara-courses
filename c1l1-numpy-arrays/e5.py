import numpy as np
p = np.array([120, 80, 45, 300, 15])
print(p > 50)
print(p[p > 50])
print((p > 50).sum(), (p > 50).mean())
print(p[(p > 50) & (p < 200)])
p[p > 200] = 200
print(p)
