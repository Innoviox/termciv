import random
from dataclasses import dataclass
from enum import Enum
from typing import List

resources = {'diamond': '💎'}

colors = {
    'F': '1;32;40',
    'G': '1;36;43',
    'I': '1;31;40',
    'S': '1;34;44',
    'H': '1;35;44',
    '0': '0'
}
color = lambda i: '\033[' + colors[i] + 'm'

@dataclass
class Tile:
    food: int
    gold: int
    industry: int
    science: int
    happiness: int
    resource: str

    @classmethod
    def generate(cls):
        f, g, i, s, h = [int(random.random() * random.randint(1, 6)) for _ in range(5)]

        if random.random() > 0.99:
            r = resources['diamond']
        else:
            r = ' '


        return cls(f, g, i, s, h, r)

    def __str__(self):
        '''
            H
        F       I
            R
        G       S
        '''
        s = ""
        s += f"   {color('H')}{self.happiness}{color('0')}   "
        s += f"{color('F')}{self.food}{color('0')}       {color('I')}{self.industry}{color('0')}"
        s += f"   {self.resource}   "
        s += f"{color('F')}{self.food}{color('0')}       {color('I')}{self.industry}{color('0')}"
        return s


class Map:
    def __init__(self, size):
        self.map = [[Tile.generate() for _ in range(size)] for _ in range(size)]

    def at(self, x, y):
        return self.map[x][y]