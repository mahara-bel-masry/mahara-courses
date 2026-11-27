import logging

import pandas as pd

logger = logging.getLogger("etl")


def clean_orders(df):
    df = df.copy()
    for col in ["order_id", "customer_id", "product"]:
        df[col] = df[col].str.strip()

    before = len(df)
    df = df.drop_duplicates(
        subset=[
            "order_id", "customer_id", "order_date",
            "product", "qty", "price",
        ]
    )
    dropped = before - len(df)
    if dropped:
        logger.info("dropped %d exact duplicate rows", dropped)

    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d")
    logger.info("cleaned: %d rows remain", len(df))
    return df
