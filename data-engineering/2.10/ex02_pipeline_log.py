import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("orders")


def clean(rows):
    kept = []
    for row in rows:
        if row["price"] is None:
            log.warning("skip %s: price missing", row["id"])
            continue
        kept.append(row)
    log.info("kept %d of %d rows", len(kept), len(rows))
    return kept


rows = [{"id": "A1", "price": 10.5}, {"id": "A2", "price": None}, {"id": "A3", "price": 7.0}]
clean(rows)
