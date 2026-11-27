import numpy as np
a = np.array([1, 2, 3])
b = np.array([1.5, 2, 3])
c = np.array([1, "x", 3])
print(a.dtype, b.dtype, c.dtype)
d = a.astype(float)
print(d, d.dtype)
print(np.array([1, 2, 3], dtype=np.int8) * 100)
