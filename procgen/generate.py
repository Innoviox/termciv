from collections import defaultdict, Counter


class Node():
    def __init__(self, distribution):
        self.distribution = distribution

    def update_distribution(self, distribution):
        self.distribution = distribution

    def collapse(self):
        ...


class World():
    def __init__(self, width, height, default_distribution, constraints):
        self.world = []
        for row in range(height):
            self.world.append([])
            for col in range(width):
                self.world.append(Node(default_distribution))

        self.constraints = constraints

    def generate(self):
        ...

    @staticmethod
    def from_string(s):
        world = s.split("\n")[1:]

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

        return World(len(world[0]), len(world), counts, constraints)


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
LLLLLLLLLLLLLLLLLLLLLLLLLLSLLLLLLL"""

w = World.from_string(world)
