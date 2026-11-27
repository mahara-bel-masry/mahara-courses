import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
rng = np.random.default_rng(6)
n = 200
df = pd.DataFrame({"size": rng.uniform(50, 200, n),
    "city": rng.choice(["cairo", "giza", "fayoum"], n)})
bump = df["city"].map({"cairo": 40, "giza": 20,
    "fayoum": 0})
noise = rng.normal(0, 10, n)
df["price"] = 10 + 1.5 * df["size"] + bump + noise
enc = OneHotEncoder()
ct = ColumnTransformer([("city", enc, ["city"])],
                       remainder="passthrough")
pipe = make_pipeline(ct, LinearRegression())
pipe.fit(df[["size", "city"]], df["price"])
print(list(pipe[0].get_feature_names_out()))
print("coef", pipe[-1].coef_.round(1))
new = pd.DataFrame({"size": [100], "city": ["unknown_city"]})
try:
    pipe.predict(new)
except ValueError as e:
    print("error:", str(e)[:60])
