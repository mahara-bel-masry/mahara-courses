calls = {"n": 0}
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("down")
    return "ok"
def retry(fn, tries=4):
    for i in range(tries):
        try:
            return fn()
        except ConnectionError:
            pass
    raise RuntimeError("gave up")
print(retry(flaky), calls["n"])
