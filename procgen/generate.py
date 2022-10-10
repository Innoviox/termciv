from collections import defaultdict, Counter

class Node():
    def __init__(self, distribution):
        self.distribution = distribution

    def update_distribution(self, distribution):
        self.distribution = distribution

    def collapse(self):
        ...

world = """
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLWWLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLWWWLWLLLLLLLLLLLLLL
LLLLLLLLLLLLLWWWWLLWLLLLLLLLLLLLLL
LLLLLLLLLLLWWWWWWWLWLLLLLLLLLLLLLL
LLLLLLLLLLWWWWWWWWWWLLLLLLLLLLLLLL
LLLLLLLWWWWWWWWWWWWWLLLLLLLLLLLLLL
LLLLLWWWWWWWWWWWWWWWWWLLLLSSSLLLLL
LLLLLLLWWWWWLLWWWWWLLLLLLSSSSLLLLL
LLLLLLLLLWWWLLWWWWWLLLLLSSSSSSLLLL
LLLLLLLLLLWWWWWWWWLLLLLLLSSSLLLLLL
LLLLLLLLLLLLWWWLLLLLLLLLLLSLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLSLLLLLLL""".split("\n")[1:]


counts = Counter()
constraints = defaultdict(lambda: defaultdict(Counter))

deltas = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == 0 and j == 0)]

for i, row in enumerate(world):
    counts.update(row)
    for j, col in enumerate(row):
        for (dx, dy) in deltas:
            if i + dy < 0 or i + dy >= len(world) or j + dx < 0 or j + dx >= len(row):
                continue

            constraints[col][(dx, dy)].update(world[i + dy][j + dx])
            # print(i, j, world[i + dy][j + dx])
        # input()

