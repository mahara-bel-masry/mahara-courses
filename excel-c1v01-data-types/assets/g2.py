# find numbers stored as text. dtype=object keeps cells as they are:
# plain read_excel quietly converts text numbers and hides the problem
import pandas as pd
df = pd.read_excel("data/raw.xlsx", dtype=object)
print("types of qty cells:", df["qty"].map(lambda v: type(v).__name__).value_counts().to_dict())
bad = df[df["qty"].map(lambda v: isinstance(v, str))]
print("rows with text qty:", list(bad["order_id"]))
df["qty"] = pd.to_numeric(df["qty"]); df["unit_price"] = pd.to_numeric(df["unit_price"])
print("types of qty cells:", df["qty"].map(lambda v: type(v).__name__).value_counts().to_dict())
print("total qty after fix:", int(df["qty"].sum()))
print("revenue after fix:", int((df["qty"]*df["unit_price"]).sum()))
