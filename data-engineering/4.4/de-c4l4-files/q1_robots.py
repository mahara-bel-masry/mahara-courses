from urllib.robotparser import RobotFileParser
rules = """User-agent: *
Disallow: /private/
""".splitlines()
rp = RobotFileParser()
rp.parse(rules)
print(rp.can_fetch("*", "http://example.local/products"))
print(rp.can_fetch("*", "http://example.local/private/data"))
