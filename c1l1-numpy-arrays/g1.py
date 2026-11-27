import numpy as np
d = np.array([[1.0, 2.0], [3.0, 4.0]])
inv = np.linalg.inv(d)
print(inv)
print(np.round(d @ inv, 6))
print(np.linalg.det(d))
w = np.array([0.5, 2.0])
x = np.array([4.0, 3.0])
print(w @ x, np.dot(w, x))
