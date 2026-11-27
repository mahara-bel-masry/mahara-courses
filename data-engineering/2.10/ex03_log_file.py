import logging

logging.basicConfig(filename="pipeline.log", level=logging.INFO, format="%(levelname)s %(message)s")
logging.info("run started")
try:
    int("abc")
except ValueError:
    logging.exception("bad number")
logging.info("run finished")
print(open("pipeline.log").read().splitlines()[0:3])
