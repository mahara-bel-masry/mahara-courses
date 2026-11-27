def clean(rows):
    return [r for r in rows if r["city"] and r["amount"] >= 0]
def test_drops_missing_city():
    assert clean([{"city": None, "amount": 5}]) == []
def test_drops_negative():
    assert clean([{"city": "a", "amount": -1}]) == []
def test_keeps_good():
    assert len(clean([{"city": "a", "amount": 1}])) == 1
