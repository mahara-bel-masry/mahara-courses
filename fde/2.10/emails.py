def normalize(text):
    return text.strip().lower()


def is_valid(text):
    return "@" in text and "." in text.split("@")[-1]
