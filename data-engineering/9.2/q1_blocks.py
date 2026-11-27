DATA = "abcdefghij"
SIZE = 4
blocks = [DATA[i:i + SIZE] for i in range(0, len(DATA), SIZE)]
print(blocks)
NODES = ["n1", "n2", "n3"]
placed = {b: NODES[i % 3] for i, b in enumerate(blocks)}
print(placed)
print("".join(blocks) == DATA)
