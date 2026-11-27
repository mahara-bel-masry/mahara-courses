gb = 50
before = gb / 1000 * 5
after = gb * 0.1 / 1000 * 5
saving = round((1 - after / before) * 100)
adr = {"decision": "partition by date", "saving_pct": saving}
print(round(before, 3), round(after, 3))
print(adr)
