import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("customers")


class BadEmail(Exception):
    pass


def parse_email(text):
    text = text.strip().lower()
    if "@" not in text:
        raise BadEmail(text)
    return text


for raw in [" Mona@Example.com ", "no-at-sign", "ali@example.com"]:
    try:
        log.info("ok: %s", parse_email(raw))
    except BadEmail as error:
        log.error("bad email: %s", error)
