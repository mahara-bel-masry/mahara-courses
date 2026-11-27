ROWS = [(1, "Cairo", 10), (2, None, 20), (3, "Giza", -5)]
def no_nulls(rows):
    return [r for r in rows if r[1] is None]
def positive(rows):
    return [r for r in rows if r[2] <= 0]
print(len(no_nulls(ROWS)))
print(len(positive(ROWS)))
print(len(no_nulls(ROWS)) + len(positive(ROWS)) == 0)
