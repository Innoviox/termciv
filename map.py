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
        continents = 2 # random.randint(2, 4)
        per = width // continents

        self.map = [[Tile.generate('ocean') for _ in range(width)] for _ in range(height)]

        for continent in range(1, continents + 1):
            cont = []
            # generate continent focus
            fx, fy = (random.randint((continent - 1) * per, continent * per), random.randint(height // 4, 3 * height // 4))
            self.map[fy][fx] = Tile.generate('city')
            # expand continent focus
            for exp in range(random.randint(500, 1000)):
                fx += random.choice([-1, 0, 1])
                fy += random.choice([-1, 0, 1])
                if fx >= width:
                    fx %= width
                if fy >= height:
                    fy %= height
                try:
                    self.map[fy][fx] = Tile.generate('desert')
                    cont.append((fx, fy))
                except IndexError:
                    pass
            #smooth continent
            cix, ciy = min(i[0] for i in cont), min(i[1] for i in cont)
            cax, cay = max(i[0] for i in cont), max(i[1] for i in cont)

            for x in range(cix, cax):
                for y in range(ciy, cay):
                    if self.map[y][x].t == 'ocean':
                        n = 0
                        for a in [-1, 0, 1]:
                            for b in [-1, 0, 1]:
                                if self.map[y+a][x+b].t == 'desert':
                                    n += 1
                        if n > 4:
                            # pass
                            self.map[y][x] = Tile.generate('desert')

    def at(self, x, y):
        return self.map[x][y]