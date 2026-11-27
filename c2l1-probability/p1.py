import numpy as np
rng = np.random.default_rng(1)
for n in (10, 100, 1000, 100000):
    rolls = rng.integers(1, 7, size=(n, 2))
    print(n, "share of sum seven", round((rolls.sum(axis=1) == 7).mean(), 4))
print("exact", round(6 / 36, 4))
flips = rng.integers(0, 2, 20)
print("20 flips", flips.tolist(), "heads", int(flips.sum()))
streak = 1; best = 1
for a, b in zip(flips[:-1], flips[1:]):
    streak = streak + 1 if a == b else 1
    best = max(best, streak)
print("longest streak", best)
runs = rng.integers(0, 2, (20000, 20))
def longest(r):
    best = cur = 1
    for a, b in zip(r[:-1], r[1:]):
        cur = cur + 1 if a == b else 1
        best = max(best, cur)
    return best
share = np.mean([longest(r) >= 5 for r in runs])
print("share of 20-flip runs with a streak of 5 or more", round(share, 3))
