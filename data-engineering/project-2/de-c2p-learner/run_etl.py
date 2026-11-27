import argparse
import logging
import sys

from etl.errors import ConfigError
from etl.logging_setup import setup_logging
from etl.pipeline import ETLPipeline, load_config


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="ETL tool: clean and report orders"
    )
    parser.add_argument("--config", default="config.json")
    parser.add_argument(
        "--input-dir", help="override config input_dir"
    )
    parser.add_argument(
        "--out-dir", help="override config out_dir"
    )
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
    except ConfigError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return 2

    if args.input_dir:
        config["input_dir"] = args.input_dir
    if args.out_dir:
        config["out_dir"] = args.out_dir
    import os
    config["log_file"] = os.path.join(
        config["out_dir"], os.path.basename(config["log_file"])
    )

    logger = setup_logging(config["log_file"])
    try:
        pipeline = ETLPipeline(config)
        code = pipeline.run()
    except ConfigError as exc:
        logger.error("config error: %s", exc)
        return 2
    except Exception:
        logging.getLogger("etl").exception(
            "pipeline crashed"
        )
        return 2

    print(f"exit code: {code}")
    return code


if __name__ == "__main__":
    sys.exit(main())
