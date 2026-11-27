from emails import is_valid, normalize


def test_normalize():
    assert normalize("  Mona@Example.COM ") == "mona@example.com"


def test_valid():
    assert is_valid("ali@example.com")


def test_invalid():
    assert not is_valid("ali@example")
