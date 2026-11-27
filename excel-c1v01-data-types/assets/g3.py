# dates are numbers: serial 1 = 1900-01-01 in the Excel system
import datetime as dt
base = dt.date(1899, 12, 30)   # Excel serial base that works for modern dates
for d in [dt.date(2026,11,1), dt.date(2026,11,27), dt.date(2026,12,31)]:
    print(d, "-> serial", (d - base).days)
print("difference:", (dt.date(2026,11,27) - dt.date(2026,11,1)).days, "days")
print("text date 27/11/2026 is not a number until parsed:")
print(dt.datetime.strptime("27/11/2026", "%d/%m/%Y").date())
