import time
import numpy as np

n = 1_000_000
lst = list(range(n))
arr = np.arange(n)

def best(f, reps=5):
    t = []
    for _ in range(reps):
        t0 = time.perf_counter()
        r = f()
        t.append(time.perf_counter() - t0)
    return min(t), r

t_list, s1 = best(lambda: sum([x * 2 for x in lst]))
t_arr, s2 = best(lambda: (arr * 2).sum())
print(s1 == s2, t_list > 5 * t_arr)
