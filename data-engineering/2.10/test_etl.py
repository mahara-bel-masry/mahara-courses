import pandas as pd
import pytest

from etl import DataValidationError, clean_orders, main, validate


@pytest.fixture
def good_df():
    return pd.DataFrame(
        {
            "id": ["ORD-1", "ORD-2", "ORD-2"],
            "qty": [1, 2, 2],
            "price": [10.0, 20.0, 20.0],
        }
    )


def test_clean_orders_drops_exact_duplicate(good_df):
    cleaned = clean_orders(good_df)
    assert len(cleaned) == 2
    assert cleaned["id"].is_unique


def test_validate_accepts_good_data(good_df):
    validate(good_df)  # must not raise


@pytest.mark.parametrize(
    "row",
    [
        {"id": "ORD-9", "qty": -1, "price": 5.0},
        {"id": "ORD-10", "qty": -3, "price": 9.0},
        {"id": "ORD-11", "qty": -100, "price": 0.5},
    ],
)
def test_validate_rejects_negative_qty(row):
    df = pd.DataFrame([row])
    with pytest.raises(DataValidationError, match="negative qty"):
        validate(df)


def test_validate_rejects_missing_column():
    df = pd.DataFrame({"id": ["ORD-1"], "qty": [1]})
    with pytest.raises(DataValidationError, match="missing columns"):
        validate(df)


def test_main_exit_code_on_bad_input(tmp_path, caplog):
    bad = tmp_path / "bad.csv"
    bad.write_text("id,qty,price\nORD-1,-2,9.99\n")
    out = tmp_path / "out.csv"
    import os

    os.makedirs("out", exist_ok=True)
    code = main(["etl.py", str(bad), str(out)])
    assert code == 1
    assert "negative qty" in caplog.text
    assert not out.exists()


def test_main_exit_code_on_missing_file(tmp_path):
    code = main(["etl.py", str(tmp_path / "nope.csv"), "x.csv"])
    assert code == 2


def test_main_writes_export_on_good_input(tmp_path):
    good = tmp_path / "good.csv"
    good.write_text("id,qty,price\nORD-1,2,9.99\nORD-2,1,\n")
    out = tmp_path / "out.csv"
    code = main(["etl.py", str(good), str(out)])
    assert code == 0
    df = pd.read_csv(out)
    assert len(df) == 2
    assert df["price_missing"].tolist() == [False, True]
