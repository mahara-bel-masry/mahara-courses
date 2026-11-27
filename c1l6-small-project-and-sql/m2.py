import pandas as pd, numpy as np
df = pd.read_csv("/tmp/shop_clean.csv")
print(df[["ads", "visitors", "sales"]].corr().round(2))
print(df.groupby("branch")["sales"].agg(["count", "mean", "median"]).round(1))
q1, q3 = df.sales.quantile([.25, .75]); iqr = q3 - q1
low = df.sales < q1 - 1.5 * iqr
high = df.sales > q3 + 1.5 * iqr
print("sales outliers by IQR", int((low | high).sum()))
