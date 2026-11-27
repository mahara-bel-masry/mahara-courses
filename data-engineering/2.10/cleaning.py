def total_price(rows):
    return round(sum(r["price"] for r in rows if r["price"] is not None), 2)


def valid_id(value):
    return isinstance(value, str) and value.startswith("ORD-")
