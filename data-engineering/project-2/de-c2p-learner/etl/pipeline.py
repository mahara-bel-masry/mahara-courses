import json
import logging
import os

from .clean import clean_orders
from .errors import ConfigError
from .export import write_outputs
from .ingest import read_customers, read_orders
from .logging_setup import setup_logging
from .transform import build_outputs
from .validate import validate_orders

logger = logging.getLogger("etl")

REQUIRED_CONFIG_KEYS = [
    "input_dir", "input_glob", "customers_file",
    "out_dir", "log_file", "rules",
]


class ETLPipeline:
    def __init__(self, config):
        missing = [
            k for k in REQUIRED_CONFIG_KEYS if k not in config
        ]
        if missing:
            raise ConfigError(f"config missing keys: {missing}")
        self.config = config

    def run(self):
        cfg = self.config
        orders_raw = read_orders(
            cfg["input_dir"], cfg["input_glob"]
        )
        customers = read_customers(
            os.path.join(
                cfg["input_dir"],
                cfg["customers_file"]
            )
        )
        orders_clean = clean_orders(orders_raw)
        accepted, rejected = validate_orders(
            orders_clean, customers, cfg["rules"]
        )
        if len(accepted) == 0:
            logger.error(
                "no accepted rows - nothing to export"
            )
            return 1
        orders, monthly, per_customer = build_outputs(
            accepted, customers
        )
        write_outputs(
            orders, monthly, per_customer,
            rejected, cfg["out_dir"]
        )
        logger.info(
            "pipeline done: %d accepted, %d rejected",
            len(orders), len(rejected)
        )
        return 0


def load_config(path):
    if not os.path.exists(path):
        raise ConfigError(f"config file not found: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)
