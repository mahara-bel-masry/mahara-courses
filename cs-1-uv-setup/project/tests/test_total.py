from inventory_tool import total_value


def test_total_value():
    assert total_value([12.5, 3.0, 40.0], [4, 10, 2]) == 160.0


def test_empty():
    assert total_value([], []) == 0
