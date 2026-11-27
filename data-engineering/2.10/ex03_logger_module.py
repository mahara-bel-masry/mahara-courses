import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s "
           "%(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

etl_log = logging.getLogger("etl")
db_log = logging.getLogger("db")

etl_log.info("reading data/orders.csv")
db_log.info("connecting to the warehouse")
etl_log.warning("ORD-7004 has no status record")

# the name column tells you WHICH part of the system spoke,
# so a warning from etl is never confused with one from db
