# Exercise: your own house-price model (C3 L1)

Task
1. Invent a price formula of your own: price depends on size and age plus random noise. Generate 300 rows with numpy default_rng and a fixed seed.
2. Split with train_test_split (test_size 0.25, random_state 0).
3. Build a baseline with DummyRegressor and record its MAE on the test set.
4. Fit LinearRegression, then a Pipeline with StandardScaler and Ridge. Record MAE, RMSE and R squared on the test set.
5. Compare the two models with 5-fold cross validation (cross_val_score, scoring r2).
6. Add a leak column computed from the price, refit, and say what happens to the test R squared and why that is a warning, not a win.

Rules: the data is invented, so state that in your write-up and do not generalise to real prices.
Solution: ex1.py (run on Python 3.13.18, output in ex1.out). Your numbers will differ if your formula differs.
