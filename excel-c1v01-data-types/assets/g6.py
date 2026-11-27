# a 5-check data quality gate before any analysis
import pandas as pd
df = pd.read_excel("data/raw.xlsx", dtype=object)
df["qty"] = pd.to_numeric(df["qty"]); df["unit_price"] = pd.to_numeric(df["unit_price"])
checks = {
 "no duplicate order_id": df["order_id"].is_unique,
 "no empty cells": not df.isna().any().any(),
 "qty is whole and positive": bool((df["qty"] > 0).all()),
 "dates are real dates": bool(df["order_date"].map(lambda v: hasattr(v, "year")).all()),
 "price is numeric": bool(df["unit_price"].map(lambda v: isinstance(v,(int,float))).all()),
}
for k, v in checks.items(): print("PASS" if v else "FAIL", "-", k)
