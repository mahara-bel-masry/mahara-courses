import logging

import pandas as pd

logger = logging.getLogger("etl")


def validate_orders(df, customers, rules):
    known_customers = set(customers["customer_id"])
    accepted_rows = []
    rejected_rows = []

    for row in df.itertuples(index=False):
        reasons = []
        if pd.isna(row.qty):
            reasons.append("qty not a number")
        elif row.qty < rules["min_qty"]:
            reasons.append(f"qty below minimum ({row.qty})")
        elif row.qty > rules["max_qty"]:
            reasons.append(f"qty above maximum ({row.qty})")

        if pd.isna(row.price):
            reasons.append("missing price")
        elif row.price < rules["min_price"]:
            reasons.append(f"price below minimum ({row.price})")

        if row.customer_id not in known_customers:
            reasons.append(
                f"unknown customer {row.customer_id}"
            )

        if reasons:
            rejected_rows.append(
                {
                    **row._asdict(),
                    "reasons": "; ".join(reasons),
                }
            )
            logger.warning(
                "REJECTED %s: %s",
                row.order_id, "; ".join(reasons)
            )
        else:
            accepted_rows.append(row._asdict())

    accepted = pd.DataFrame(
        accepted_rows, columns=df.columns
    )
    rejected = pd.DataFrame(rejected_rows)
    logger.info(
        "validation: %d accepted, %d rejected",
        len(accepted), len(rejected)
    )
    return accepted, rejected
