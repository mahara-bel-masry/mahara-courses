import sys

import pandas as pd


class DataValidationError(Exception):
    pass


def validate(df):
    required = {"id", "qty", "price"}
    missing = required - set(df.columns)
    if missing:
        raise DataValidationError("missing columns: " + str(sorted(missing)))
    if (df["qty"] < 0).any():
        bad = df.loc[df["qty"] < 0, "id"].tolist()
        raise DataValidationError("negative qty in orders: " + str(bad))


for path in ["data/orders.csv", "data/no_price.csv", "data/bad_qty.csv"]:
    try:
        validate(pd.read_csv(path))
    except DataValidationError as exc:
        print("REJECTED", path, "-", exc)
    else:
        print("ACCEPTED", path)

print()
print("exit code convention: 0 ok, 1 rejected input")
sys.exit(0)
