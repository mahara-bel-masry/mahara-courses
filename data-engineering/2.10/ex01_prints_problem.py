# why print alone is not enough
# for a pipeline that runs unattended
import pandas as pd

df = pd.read_csv("data/orders.csv")

print("rows loaded:", len(df))
print("WARNING: ORD-7004 has no status record")
print("done")

# questions nobody can answer tomorrow from this output:
# WHEN did this run? WHICH script said it?
# HOW severe is it?
