stock = 3
while stock > 0:
    print("selling, left:", stock - 1)
    stock -= 1
for n in [4, 9, 12, 5]:
    if n > 10:
        print("found big:", n)
        break
    if n < 5:
        continue
    print("checked", n)
