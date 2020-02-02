import random
from dataclasses import dataclass
from enum import Enum
from typing import List

class Resource(Enum):
    MARBLE = 1
    # todo add cool names/generate


@dataclass
class Tile:
    food: float
    gold: float
    industry: float
    science: float
    happiness: float
    resources: List[Resource]

    @classmethod
    def generate(cls):
        f, g, i, s, h = [random.random() * random.randint(1, 5) + random.uniform(0, 2) for _ in range(5)]

        r = []
        if random.random() > 0.99: r.append(Resource.MARBLE)

        return cls(f, g, i, s, h, r)

class Map:
    def __init__(self, size):
        self.map = [[Tile.generate() for _ in range(size)] for _ in range(size)]