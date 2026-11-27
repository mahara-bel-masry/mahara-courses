import logging

import pandas as pd

logger = logging.getLogger("etl")


def build_outputs(accepted, customers):
    df = accepted.merge(customers, on="customer_id", how="left")
    df["total"] = (df["qty"] * df["price"]).round(2)
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    monthly = (
        df.groupby("month")
        .agg(orders=("order_id", "count"), revenue=("total", "sum"))
        .round(2)
        .reset_index()
    )
    per_customer = (
        df.groupby(["customer_id", "name", "city"])
        .agg(orders=("order_id", "count"), revenue=("total", "sum"))
        .round(2)
        .reset_index()
    )
    logger.info(
        "transform: %d accepted orders, total revenue %.2f",
        len(df),
        df["total"].sum(),
    )
    return df, monthly, per_customer
