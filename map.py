import random
from dataclasses import dataclass
from enum import Enum
from typing import List

resources = {'diamond': '💎'}

terrain = {
    'desert': (0, 0.1, 2.5, 1.0, -0.2),
    'forest': (3, 0, 2, 1, 1),
    'ocean': (1, 0, 0, 0, 0),
    'plains': (1, 1, 1, 1, 1),
    'mountain': (0.5, 2, 1, 3, 0.5),
    'city': (5, 5, 5, 5, 5)
}

@dataclass
class Tile:
    f: int # food
    g: int # gold
    i: int # industry
    s: int # science
    h: int # happiness
    r: str # resource
    t: str # terrain

    @classmethod
    def generate(cls, t):
        f, g, i, s, h = [int(random.random() * random.randint(1, 6)) for _ in range(5)]

        if random.random() > 0.99:
            r = resources['diamond']
        else:
            r = ' '

        a, b, c, d, e = terrain[t]


        return cls(f * a, g * b, i * c, s * d, h * e, r, t)


class Map:
    def __init__(self, width, height):
        continents = 5 # random.randint(2, 4)
        per = width // continents

        self.map = [[Tile.generate('ocean') for _ in range(width)] for _ in range(height)]

        for continent in range(1, continents + 1):
            # generate continent focus
            fx, fy = (random.randint((continent - 1) * per, continent * per), random.randint(0, height))
            self.map[fy][fx] = Tile.generate('city')
            # expand continent focus
            for exp in range(random.randint(50, 100)):
                fx += random.choice([-1, 0, 1])
                fy += random.choice([-1, 0, 1])
                if fx >= width:
                    fx %= width
                if fy >= height:
                    fy %= height
                try:
                    self.map[fy][fx] = Tile.generate('desert')
                except IndexError:
                    pass




    def at(self, x, y):
        return self.map[x][y]