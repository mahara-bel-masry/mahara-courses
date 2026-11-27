rows_per_day = 1_000_000
bytes_per_row = 200
GB_MONTH = 0.02     # assumed dollars per GB per month
RUN_HOUR = 0.50     # assumed dollars per pipeline hour
gb = rows_per_day * 30 * bytes_per_row / 1e9
storage = gb * GB_MONTH
compute = 30 * 0.5 * RUN_HOUR
print(round(gb, 1))
print(round(storage, 2))
print(round(compute, 2))
print(round(storage + compute, 2))
