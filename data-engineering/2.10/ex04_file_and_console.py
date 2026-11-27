import logging

logger = logging.getLogger("etl")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

logfile = logging.FileHandler("out/etl.log", mode="w")
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)-8s %(name)s: %(message)s")
)

logger.addHandler(console)
logger.addHandler(logfile)

logger.debug("connection details for developers")
logger.info("pipeline started")
logger.warning("ORD-7004 has no status record")
logger.info("pipeline finished")

# console stays short and readable,
# out/etl.log keeps time, level and logger name
