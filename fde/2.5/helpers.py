def clean_name(text):
    return text.strip().title()


def paid_total(rows):
    return sum(float(r["total"]) for r in rows if r["status"] == "paid")
