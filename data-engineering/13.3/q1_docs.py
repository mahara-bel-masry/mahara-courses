import inspect

def clean(xs):
    """Drop empty values from a list."""
    return [x for x in xs if x]

def test_clean():
    assert clean([1, 0, 2]) == [1, 2]

test_clean()
print("test passed")
print(inspect.getdoc(clean))
