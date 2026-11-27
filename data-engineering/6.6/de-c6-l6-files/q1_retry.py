import logging
logging.basicConfig(format="%(levelname)s %(message)s", level=logging.INFO)
n = {"calls": 0}
def flaky():
    n["calls"] += 1
    if n["calls"] < 3:
        raise ConnectionError("down")
    return "data"
def retry(fn, tries=3):
    for k in range(1, tries + 1):
        try:
            return fn()
        except ConnectionError:
            logging.warning("try %d failed", k)
    return None
print(retry(flaky))
print(n["calls"])
