def total_value(prices, quantities):
    """Return the total stock value."""
    return sum(p * q for p, q in zip(prices, quantities))


def main() -> None:
    prices = [12.5, 3.0, 40.0]
    quantities = [4, 10, 2]
    print(f"stock value = {total_value(prices, quantities):.2f}")
