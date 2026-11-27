import random
random.seed(1)
cities = ["cairo", "giza", "alex", "luxor"]
with open("/tmp/big/sales.csv", "w") as f:
    f.write("id,city,amount\n")
    for i in range(1, 29_000_001):
        f.write(f"{i},{cities[i % 4]},{random.randint(1, 500)}\n")
