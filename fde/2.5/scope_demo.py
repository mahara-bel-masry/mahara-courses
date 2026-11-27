def total(prices):
    result = 0
    for p in prices:
        result += p
    return result


print(total([10, 20, 30]))
try:
    print(result)
except NameError as error:
    print("NameError:", error)
