import numpy as np
x = np.arange(12)
print(x)
m = x.reshape(3, 4)
print(m)
print(m.shape, m.ndim, m.size)
print(m.reshape(2, -1).shape)
print(m.T.shape)
print(m.flatten())
