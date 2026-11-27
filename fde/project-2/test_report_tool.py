import pandas as pd
from report_tool import clean_customers, build_report

def test_clean_removes_duplicate_and_bad():
    df = pd.DataFrame({"name": [" a ", "A", "b"], "email": ["X@a.com", "x@a.com ", "bad"], "city": ["C", "C", None]})
    out = clean_customers(df)
    assert out["email"].tolist() == ["x@a.com"]

def test_report_totals():
    c = pd.DataFrame({"email": ["x@a.com", "y@a.com"], "name": ["X", "Y"], "city": ["C", "C"]})
    o = pd.DataFrame({"email": ["x@a.com", "x@a.com"], "amount": [1, 2]})
    r = build_report(c, o)
    assert r["amount"].tolist() == [3, 0]

def test_missing_city_filled():
    df = pd.DataFrame({"name": ["b"], "email": ["b@a.com"], "city": [None]})
    assert clean_customers(df)["city"].iloc[0] == "Unknown"
