import numpy as np
rng = np.random.default_rng(3)
n = 100000
pop = 1000
sick = rng.random(n) < 0.01
pos = np.where(sick, rng.random(n) < 0.95, rng.random(n) < 0.05)
print("share sick", round(sick.mean(), 4))
print("P(positive)", round(pos.mean(), 4))
print("P(sick | positive)", round(sick[pos].mean(), 4))
tp = (sick & pos).sum(); fp = (~sick & pos).sum()
print("true positives", int(tp), "false positives", int(fp))
exact = 0.01 * 0.95 / (0.01 * 0.95 + 0.99 * 0.05)
print("Bayes exact", round(exact, 4))
