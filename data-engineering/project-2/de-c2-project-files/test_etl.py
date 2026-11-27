import pandas as pd
from etl import transform


def test_strip_and_title():
    df = pd.DataFrame({"id": ["A"], "customer": [" mona "], "qty": [1], "price": ["5"]})
    assert transform(df)["customer"].iloc[0] == "Mona"


def test_drops_duplicates_and_missing():
    df = pd.DataFrame({"id": ["A", "A", "B"], "customer": ["x", "x", "y"], "qty": [1, 1, 1], "price": [1.0, 1.0, None]})
    assert len(transform(df)) == 1


def test_total():
    df = pd.DataFrame({"id": ["A"], "customer": ["x"], "qty": [3], "price": [2.5]})
    assert transform(df)["total"].iloc[0] == 7.5
