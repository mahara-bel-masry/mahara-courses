import argparse, json, logging
import pandas as pd
from pypdf import PdfReader

log = logging.getLogger("report")

def load_config(path):
    with open(path) as f:
        return json.load(f)

def clean_customers(df):
    df = df.copy()
    df["email"] = df["email"].str.strip().str.lower()
    df["name"] = df["name"].str.strip().str.title()
    df["city"] = df["city"].fillna("Unknown")
    bad = ~df["email"].str.contains("@")
    for e in df.loc[bad, "email"]:
        log.error("bad email: %s", e)
    df = df[~bad].drop_duplicates(subset="email")
    log.info("customers kept: %d", len(df))
    return df

def read_orders(path):
    text = PdfReader(path).pages[0].extract_text()
    rows = []
    for line in text.splitlines():
        _, email, amount = line.split()
        rows.append({"email": email, "amount": int(amount)})
    log.info("orders read: %d", len(rows))
    return pd.DataFrame(rows)

def build_report(customers, orders):
    totals = orders.groupby("email")["amount"].sum().reset_index()
    merged = customers.merge(totals, on="email", how="left").fillna({"amount": 0})
    return merged

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="config.json")
    p.add_argument("--out")
    a = p.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    cfg = load_config(a.config)
    out = a.out or cfg["out"]
    rep = build_report(clean_customers(pd.read_csv(cfg["csv"])), read_orders(cfg["pdf"]))
    rep["amount"] = rep["amount"].astype(int)
    rep.to_json(out, orient="records")
    log.info("report written: %s", out)

if __name__ == "__main__":
    main()
