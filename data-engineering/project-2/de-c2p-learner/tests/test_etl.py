import json
import os
import sys

import pandas as pd
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl.clean import clean_orders
from etl.ingest import read_customers, read_orders
from etl.pipeline import ETLPipeline, load_config
from etl.transform import build_outputs
from etl.validate import validate_orders
from run_etl import main

RULES = {"min_qty": 1, "max_qty": 1000, "min_price": 0.01}


@pytest.fixture
def customers():
    return pd.DataFrame(
        {"customer_id": ["C-001", "C-002"], "name": ["A", "B"], "city": ["X", "Y"]}
    )


@pytest.fixture
def good_row():
    return {
        "order_id": "ORD-1",
        "customer_id": "C-001",
        "order_date": "2026-01-05",
        "product": "pens",
        "qty": "2",
        "price": "10.0",
    }


def make_df(rows):
    return pd.DataFrame(rows)


def test_ingest_reads_every_matching_file(tmp_path):
    for name, n in [("orders_a.csv", 2), ("orders_b.csv", 3)]:
        pd.DataFrame(
            {
                "order_id": [f"O{i}" for i in range(n)],
                "customer_id": ["C-001"] * n,
                "order_date": ["2026-01-01"] * n,
                "product": ["p"] * n,
                "qty": ["1"] * n,
                "price": ["1.0"] * n,
            }
        ).to_csv(tmp_path / name, index=False)
    df = read_orders(str(tmp_path), "orders_*.csv")
    assert len(df) == 5
    assert set(df["source_file"]) == {"orders_a.csv", "orders_b.csv"}


def test_ingest_missing_folder_raises():
    with pytest.raises(FileNotFoundError, match="no order files"):
        read_orders("data/no_such_dir", "orders_*.csv")


def test_clean_drops_exact_duplicate_and_coerces(good_row):
    df = make_df([good_row, dict(good_row)])
    cleaned = clean_orders(df)
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["qty"] == 2
    assert cleaned.iloc[0]["price"] == 10.0


def test_clean_strips_hidden_whitespace(good_row):
    messy = dict(good_row, order_id="  ORD-9 ", customer_id=" C-001 ")
    cleaned = clean_orders(make_df([messy]))
    assert cleaned.iloc[0]["order_id"] == "ORD-9"
    assert cleaned.iloc[0]["customer_id"] == "C-001"


@pytest.mark.parametrize(
    "patch,reason_part",
    [
        ({"qty": "-3"}, "qty below minimum"),
        ({"qty": "abc"}, "qty not a number"),
        ({"price": ""}, "missing price"),
        ({"customer_id": "C-999"}, "unknown customer"),
    ],
)
def test_validate_rejects_with_named_reason(good_row, customers, patch, reason_part):
    row = dict(good_row, **patch)
    cleaned = clean_orders(make_df([row]))
    accepted, rejected = validate_orders(cleaned, customers, RULES)
    assert len(accepted) == 0
    assert len(rejected) == 1
    assert reason_part in rejected.iloc[0]["reasons"]
    assert rejected.iloc[0]["order_id"] == row["order_id"].strip()


def test_validate_accepts_clean_row(good_row, customers):
    cleaned = clean_orders(make_df([good_row]))
    accepted, rejected = validate_orders(cleaned, customers, RULES)
    assert len(accepted) == 1
    assert len(rejected) == 0


def test_transform_computes_totals_and_months(good_row, customers):
    cleaned = clean_orders(make_df([good_row, dict(good_row, order_id="ORD-2")]))
    accepted, _ = validate_orders(cleaned, customers, RULES)
    orders, monthly, per_customer = build_outputs(accepted, customers)
    assert orders["total"].tolist() == [20.0, 20.0]
    assert monthly.iloc[0]["revenue"] == 40.0
    assert per_customer.iloc[0]["orders"] == 2


def test_pipeline_end_to_end_on_repo_data(tmp_path):
    config = load_config("config.json")
    config["out_dir"] = str(tmp_path / "out")
    config["log_file"] = str(tmp_path / "out" / "etl.log")
    code = ETLPipeline(config).run()
    assert code == 0
    orders = pd.read_csv(tmp_path / "out" / "orders_clean.csv")
    rejected = pd.read_csv(tmp_path / "out" / "rejected.csv")
    assert len(orders) == 17
    assert len(rejected) == 3
    summary = json.load(open(tmp_path / "out" / "summary.json"))
    assert summary["orders_accepted"] == 17
    assert summary["total_revenue"] == 1903.25
    monthly = pd.read_excel(tmp_path / "out" / "monthly_totals.xlsx", sheet_name="monthly_totals")
    assert list(monthly["month"]) == ["2026-01", "2026-02"]


def test_pipeline_zero_accepted_returns_1(tmp_path, good_row, customers):
    bad = dict(good_row, qty="-1")
    bad_df = make_df([bad])
    bad_df.to_csv(tmp_path / "orders_x.csv", index=False)
    customers.to_csv(tmp_path / "customers.csv", index=False)
    config = {
        "input_dir": str(tmp_path),
        "input_glob": "orders_*.csv",
        "customers_file": "customers.csv",
        "out_dir": str(tmp_path / "out"),
        "log_file": str(tmp_path / "out" / "etl.log"),
        "rules": RULES,
    }
    assert ETLPipeline(config).run() == 1
    assert not os.path.exists(tmp_path / "out" / "orders_clean.csv")


def test_main_missing_config_returns_2():
    assert main(["--config", "no_such_config.json"]) == 2


def test_main_override_dirs_changes_nothing_in_code(tmp_path):
    code = main(
        [
            "--config", "config.json",
            "--input-dir", "data/raw2",
            "--out-dir", str(tmp_path / "out2"),
        ]
    )
    assert code == 0
    orders = pd.read_csv(tmp_path / "out2" / "orders_clean.csv")
    assert len(orders) == 22
