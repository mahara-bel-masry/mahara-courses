import numpy as np
from math import comb
n, p = 10, 0.3
pmf = [comb(n, k) * p**k * (1 - p)**(n - k) for k in range(n + 1)]
print("P(k) for k=0..10", [round(x, 3) for x in pmf])
print("sum of probabilities", round(sum(pmf), 6))
print("mean by formula", n * p, "by pmf", round(sum(k * x for k, x in enumerate(pmf)), 3))
print("P(at most 2)", round(sum(pmf[:3]), 4))
rng = np.random.default_rng(4)
sim = rng.binomial(n, p, 100000)
print("simulated mean", round(sim.mean(), 3), "P(at most 2)", round((sim <= 2).mean(), 4))
print("P(exactly 3)", round(pmf[3], 4), "simulated", round((sim == 3).mean(), 4))
