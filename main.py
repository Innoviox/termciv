from asciimatics.screen import Screen
from civ import Civilization
from map import Map

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.map = Map(5)

        while True:
            self.display(self.map.at(0, 0), 0, 0)
            # screen.get_key()
            screen.refresh()

    def display(self, tile, x, y):
        self.screen.print_at(f"{tile.h}", x + 3, y)
        self.screen.print_at(f"{tile.f}", x, y + 1)
        self.screen.print_at(f"{tile.i}", x + 6, y + 1)
        self.screen.print_at(f"{tile.r}", x + 4, y + 2)
        self.screen.print_at(f"{tile.g}", x, y + 3)
        self.screen.print_at(f"{tile.s}", x + 6, y + 3)


Screen.wrapper(Game)
