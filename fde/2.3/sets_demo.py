cities = ["Cairo", "Giza", "Cairo", "Alex", "Giza", "Cairo"]
unique = set(cities)
print(len(cities), len(unique))
print(sorted(unique))
paid = {"ORD-1", "ORD-2", "ORD-3"}
shipped = {"ORD-2", "ORD-3", "ORD-4"}
print(sorted(paid & shipped))
print(sorted(paid - shipped))
print("ORD-2" in paid)
