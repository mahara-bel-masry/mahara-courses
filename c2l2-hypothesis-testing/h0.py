import numpy as np
rng = np.random.default_rng(4)
# invented story: old page vs new page, minutes spent per visit
old = rng.normal(10.0, 3.0, 40)
new = rng.normal(11.2, 3.0, 40)
print("old mean", round(old.mean(), 2), "new mean", round(new.mean(), 2))
diff = new.mean() - old.mean()
print("observed difference", round(diff, 2))
# null world: labels mean nothing, shuffle them
both = np.concatenate([old, new])
count = 0
trials = 10000
for _ in range(trials):
    rng.shuffle(both)
    d = both[40:].mean() - both[:40].mean()
    if abs(d) >= abs(diff):
        count += 1
print("shuffles as extreme as observed", count, "of", trials)
print("permutation p value", count / trials)
