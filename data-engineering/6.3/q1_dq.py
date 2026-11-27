rows = [(1, 25), (2, None), (3, -5), (3, 40)]
def check(rs):
    bad = []
    seen = set()
    for i, p in rs:
        if p is None or p < 0 or i in seen:
            bad.append(i)
        seen.add(i)
    return bad
print(len(rows))
print(check(rows))
