import pytest
from cleaning import total_price, valid_id


def test_total_skips_missing():
    rows = [{"price": 10.5}, {"price": None}, {"price": 7.0}]
    assert total_price(rows) == 18.5


def test_valid_id():
    assert valid_id("ORD-7001")
    assert not valid_id("A1")


def test_total_empty():
    assert total_price([]) == 0


def test_bad_price_raises():
    with pytest.raises(TypeError):
        total_price([{"price": "x"}])
