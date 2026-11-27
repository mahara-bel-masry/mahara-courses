import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("checking row counts")
logging.info("pipeline started")
logging.warning("ORD-7004 has no status record")
logging.error("could not write the export file")
logging.critical("database is unreachable, stopping")

# every line now carries a time and a severity,
# and you can silence levels below INFO later
