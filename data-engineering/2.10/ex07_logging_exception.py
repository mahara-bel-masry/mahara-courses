import logging

import pandas as pd

logger = logging.getLogger("etl")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    "out/etl_errors.log", mode="w")
fmt = "%(asctime)s %(levelname)-8s %(message)s"
handler.setFormatter(logging.Formatter(fmt))
logger.addHandler(handler)

try:
    df = pd.read_csv("data/empty.csv")
except pd.errors.EmptyDataError:
    logger.exception("could not load the input file")
    print("load failed;")
    print("details are in out/etl_errors.log")

# logger.exception writes the message AND
# the full traceback to the log
