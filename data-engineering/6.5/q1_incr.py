src = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
target = [(1, "a"), (2, "b")]
def full(s):
    return list(s)
def incremental(s, t):
    last = max(i for i, _ in t)
    return [r for r in s if r[0] > last]
print(len(full(src)))
print(len(incremental(src, target)))
print(incremental(src, target))
