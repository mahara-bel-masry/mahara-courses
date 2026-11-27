import yaml
Y = "services:\n  db:\n    image: postgres:16\n"
Y += "  app:\n    build: .\n    depends_on: [db]\n"
d = yaml.safe_load(Y)
print(sorted(d["services"]))
print(d["services"]["app"]["depends_on"])
print(d["services"]["db"]["image"])
