def chunks(n, size):
    for s in range(0, n, size):
        yield range(s, min(s + size, n))
total = 0
count = 0
for part in chunks(100, 25):
    total += sum(part)
    count += 1
print(count)
print(total)
