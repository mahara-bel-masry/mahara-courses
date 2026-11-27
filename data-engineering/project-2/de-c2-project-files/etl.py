import argparse
import glob
import logging

import pandas as pd

log = logging.getLogger("etl")


def extract(folder):
    files = sorted(glob.glob(folder + "/*.csv"))
    log.info("found %d files", len(files))
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)


def transform(df):
    df["customer"] = df["customer"].str.strip().str.title()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    missing = df["price"].isna().sum()
    log.warning("%d rows with missing price", missing)
    df = df.dropna(subset=["price"]).drop_duplicates(subset="id")
    df["total"] = df["qty"] * df["price"]
    return df


def load(df, path):
    df.to_csv(path, index=False)
    log.info("saved %d rows to %s", len(df), path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="clean_orders.csv")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    load(transform(extract(args.input)), args.output)


if __name__ == "__main__":
    main()
