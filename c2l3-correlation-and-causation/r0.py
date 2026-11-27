import numpy as np
rng = np.random.default_rng(3)
# invented story: hours studied and exam score for 60 students
hours = rng.uniform(1, 10, 60)
score = 50 + 4 * hours + rng.normal(0, 6, 60)
r = np.corrcoef(hours, score)[0, 1]
print("correlation r", round(r, 3))
print("r squared", round(r ** 2, 3))
slope, intercept = np.polyfit(hours, score, 1)
print("slope", round(slope, 2), "intercept", round(intercept, 2))
