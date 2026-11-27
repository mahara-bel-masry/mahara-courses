import json
import logging
import os

logger = logging.getLogger("etl")


def write_outputs(orders, monthly, per_customer, rejected, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    paths = {
        "orders": os.path.join(out_dir, "orders_clean.csv"),
        "rejected": os.path.join(out_dir, "rejected.csv"),
        "monthly": os.path.join(out_dir, "monthly_totals.xlsx"),
        "summary": os.path.join(out_dir, "summary.json"),
    }
    orders.to_csv(paths["orders"], index=False)
    logger.info("wrote %s (%d rows)", paths["orders"], len(orders))

    rejected.to_csv(paths["rejected"], index=False)
    logger.info("wrote %s (%d rows)", paths["rejected"], len(rejected))

    import pandas as pd

    with pd.ExcelWriter(paths["monthly"], engine="openpyxl") as writer:
        monthly.to_excel(writer, sheet_name="monthly_totals", index=False)
        per_customer.to_excel(writer, sheet_name="per_customer", index=False)
    logger.info("wrote %s (2 sheets)", paths["monthly"])

    summary = {
        "orders_accepted": int(len(orders)),
        "orders_rejected": int(len(rejected)),
        "total_revenue": (
            float(round(orders["total"].sum(), 2))
            if len(orders)
            else 0.0
        ),
        "months": monthly.to_dict(orient="records"),
    }
    with open(paths["summary"], "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    logger.info("wrote %s", paths["summary"])
    return paths
