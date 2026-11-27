VM_HOUR = 0.10      # assumed dollars per hour
GB_MONTH = 0.02     # assumed dollars per GB per month
def monthly(hours, gb):
    return hours * VM_HOUR + gb * GB_MONTH
print(round(monthly(730, 500), 2))
print(round(monthly(100, 500), 2))
