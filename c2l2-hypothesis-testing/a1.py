from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
for new in (0.12, 0.11, 0.105):
    es = proportion_effectsize(new, 0.10)
    n = NormalIndPower().solve_power(es, alpha=0.05, power=0.8)
    print("from 0.10 to", new, "needs", int(n) + 1, "per group")
