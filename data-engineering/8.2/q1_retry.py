calls = [0]
def flaky():
    calls[0] += 1
    if calls[0] < 3:
        raise RuntimeError("fail")
    return "ok"
def run(retries):
    for i in range(retries + 1):
        try:
            return flaky()
        except RuntimeError:
            print("retry", i + 1)
    return "failed"
print(run(3))
