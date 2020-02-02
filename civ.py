from dataclasses import dataclass
from typing      import List

@dataclass
class Position:
    x: int
    y: int

@dataclass
class City:
    name: str
    pos: Position

@dataclass
class Civilization:
    name: str
    talents: int
    cities: List[City]
