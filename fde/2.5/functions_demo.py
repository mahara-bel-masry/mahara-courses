def add_vat(price, rate=0.14):
    return round(price * (1 + rate), 2)


print(add_vat(100))
print(add_vat(100, rate=0.05))
print(add_vat(price=250))


def no_return(x):
    x * 2


print(no_return(4))
