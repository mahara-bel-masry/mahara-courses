import logging
import os


def setup_logging(log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logger = logging.getLogger("etl")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-8s %(name)s %(message)s")
    )

    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger
