import numpy as np, os
m = np.arange(6).reshape(2, 3) * 1.5
np.savetxt("t.csv", m, delimiter=",", fmt="%.1f")
print(open("t.csv").read().strip())
b = np.loadtxt("t.csv", delimiter=",")
print(b.shape, np.array_equal(m, b))
np.save("t.npy", m)
print(np.array_equal(np.load("t.npy"), m))
print(np.zeros(1000, dtype=np.int8).nbytes, np.zeros(1000).nbytes)
os.remove("t.csv"); os.remove("t.npy")
