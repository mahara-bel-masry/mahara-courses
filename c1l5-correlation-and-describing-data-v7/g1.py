import numpy as np
a = np.array([4, 5, 5, 6, 7, 7, 7, 8, 9, 30])
z = (a - a.mean()) / a.std(ddof=1)
print("z scores", np.round(z, 2).tolist())
print("biggest |z|", round(abs(z).max(), 2), "for value", a[abs(z).argmax()])
q1, q3 = np.percentile(a, [25, 75]); iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("fences", lo, hi)
print("flagged by IQR", a[(a < lo) | (a > hi)].tolist())
print("flagged by |z| > 2", a[abs(z) > 2].tolist())
print("flagged by |z| > 3", a[abs(z) > 3].tolist())
