import random
from dataclasses import dataclass
from enum import Enum
from typing import List

resources = {'diamond': '💎'}

@dataclass
class Tile:
    f: int # food
    g: int # gold
    i: int # industry
    s: int # science
    h: int # happiness
    r: str # resource

    @classmethod
    def generate(cls):
        f, g, i, s, h = [int(random.random() * random.randint(1, 6)) for _ in range(5)]

        if random.random() > 0.99:
            r = resources['diamond']
        else:
            r = 'N'


        return cls(f, g, i, s, h, r)


class Map:
    def __init__(self, size):
        self.map = [[Tile.generate() for _ in range(size)] for _ in range(size)]

    def at(self, x, y):
        return self.map[x][y]