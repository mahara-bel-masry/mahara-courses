import glob
import logging
import os

import pandas as pd

logger = logging.getLogger("etl")


def read_orders(input_dir, pattern):
    files = sorted(glob.glob(os.path.join(input_dir, pattern)))
    if not files:
        raise FileNotFoundError(f"no order files matching {pattern} in {input_dir}")
    frames = []
    for path in files:
        part = pd.read_csv(path, dtype=str)
        part["source_file"] = os.path.basename(path)
        frames.append(part)
        logger.info("read %s: %d rows", path, len(part))
    combined = pd.concat(frames, ignore_index=True)
    logger.info("total rows read: %d from %d files", len(combined), len(files))
    return combined


def read_customers(customers_path):
    customers = pd.read_csv(customers_path, dtype=str)
    customers["customer_id"] = (
        customers["customer_id"].str.strip()
    )
    logger.info(
        "read %d customers from %s",
        len(customers), customers_path
    )
    return customers
