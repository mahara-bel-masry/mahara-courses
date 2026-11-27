import pandas as pd


def load(path):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print("the file does not exist:", path)
        return None
    except pd.errors.EmptyDataError:
        print("the file exists but has no columns:", path)
        return None
    else:
        print("loaded", len(df), "rows from", path)
        return df
    finally:
        print("load attempt finished for", path)


load("data/orders.csv")
print()
load("data/missing_file.csv")
print()
load("data/empty.csv")

# each except names the exact failure it handles:
# no bare except, no swallowing a bug you did not expect
