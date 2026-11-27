import numpy as np
m = np.arange(12).reshape(3, 4)
print(m[0, 0], m[2, 3], m[-1, -1])
print(m[1])
print(m[:, 2])
print(m[0:2, 1:3])
v = m[0:2, 1:3]
v[0, 0] = 99
print(m[0])
w = m[0:2, 1:3].copy()
w[0, 0] = -1
print(m[0])
