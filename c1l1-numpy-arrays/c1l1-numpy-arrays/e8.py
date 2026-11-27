import numpy as np
a = np.array([1, 2, 3])
b = a
b[0] = 100
print(a)
print(0.1 + 0.2 == 0.3, np.isclose(0.1 + 0.2, 0.3))
print(np.array([1, 2, 3]) == np.array([1, 2, 4]))
print(np.array([[1, 2], [3, 4]]) * np.array([[1, 2], [3, 4]]))
print(np.array([[1, 2], [3, 4]]) @ np.array([[1, 2], [3, 4]]))
print(np.mean([]) if False else np.array([1,2,3]).mean())
