import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
print("print has no level")
logging.debug("hidden at INFO level")
logging.info("loaded 12 rows")
logging.warning("2 missing prices")
logging.error("ORD-7004 has no status")
