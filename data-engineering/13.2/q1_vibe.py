def ai_total(xs):
    return sum(xs[:-1])
def check():
    assert ai_total([1, 2, 3]) == 6
try:
    check()
except AssertionError:
    print("bug caught")
print(sum([1, 2, 3]))
