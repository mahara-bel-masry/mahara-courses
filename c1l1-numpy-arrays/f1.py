import numpy as np
s = np.array([120, 80, 45, 300, 15])
print(np.where(s > 100, "high", "low"))
print(np.sort(s), np.argsort(s))
print(s.argmax(), s.max())
print(np.sort(s)[::-1])
