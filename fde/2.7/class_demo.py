class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def with_vat(self, rate=0.14):
        return round(self.total * (1 + rate), 2)


order = Order("A1", 100)
print(order.order_id)
print(order.with_vat())
