"""ETL with logging, validation, and explicit exit codes.

Usage: python3 assets/etl.py INPUT_CSV OUTPUT_CSV
Exit codes: 0 ok, 1 rejected input, 2 unreadable file.
"""
import logging
import sys

import pandas as pd


class DataValidationError(Exception):
    pass


def make_logger(log_path):
    logger = logging.getLogger("etl")
    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
    logfile = logging.FileHandler(log_path, mode="w")
    logfile.setLevel(logging.DEBUG)
    logfile.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    )
    logger.addHandler(console)
    logger.addHandler(logfile)
    return logger


def clean_orders(df):
    df = df.copy()
    df["id"] = df["id"].str.strip()
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(how="all")
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="id", keep="first")
    return df


def validate(df):
    required = {"id", "qty", "price"}
    missing = required - set(df.columns)
    if missing:
        raise DataValidationError(
            "missing columns: " + str(sorted(missing))
        )
    if (df["qty"] < 0).any():
        bad = df.loc[df["qty"] < 0, "id"].tolist()
        raise DataValidationError("negative qty in: " + str(bad))


def main(argv):
    if len(argv) != 3:
        print("usage: python3 assets/etl.py INPUT_CSV OUTPUT_CSV")
        return 2
    input_path, output_path = argv[1], argv[2]
    logger = make_logger("out/etl.log")
    logger.info("starting etl: %s -> %s", input_path, output_path)
    try:
        raw = pd.read_csv(input_path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        logger.exception("could not read the input file")
        return 2
    logger.info("loaded %s rows", len(raw))
    try:
        validate(raw)
    except DataValidationError as exc:
        logger.error("input rejected: %s", exc)
        return 1
    df = clean_orders(raw)
    dropped = len(raw) - len(df)
    df["price_missing"] = df["price"].isna()
    df.to_csv(output_path, index=False)
    logger.warning(
        "missing prices flagged: %s", int(df["price_missing"].sum())
    )
    logger.info("dropped %s rows, wrote %s rows", dropped, len(df))
    return 0


if __name__ == "__main__":
    import os

    os.makedirs("out", exist_ok=True)
    sys.exit(main(sys.argv))
