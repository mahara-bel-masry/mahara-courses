order = {"id": "ORD-1"}
try:
    print(order["city"])
except KeyError as error:
    print("KeyError:", error)

items = [1, 2, 3]
try:
    print(items[5])
except IndexError as error:
    print("IndexError:", error)
