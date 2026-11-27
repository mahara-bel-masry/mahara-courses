ROWS = [(1, 10), (2, 20), (3, -5)]
def extract():
    return ROWS
def check(rows):
    return all(r[1] > 0 for r in rows)
def load(rows):
    return len(rows)
def run():
    rows = extract()
    if not check(rows):
        return "alert: bad data, load skipped"
    return load(rows)
print(run())
