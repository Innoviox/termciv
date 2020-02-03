from asciimatics.screen import Screen
from civ import Civilization
from map import Map

terrain_colors = {
    'desert': 226,
    'forest': 22,
    'ocean': 19,
    'plains': 118,
    'mountain': 255
}

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.map = Map(5)

        while True:
            for i in range(5):
                for j in range(5):
                    self.display(self.map.at(i, j), i * 11, j * 6)
            # screen.get_key()
            screen.refresh()

    def display(self, tile, x, y):
        self.screen.print_at(" ", x, y, bg=terrain_colors[tile.t])
        # self.screen.print_at("┌─────────┐", x, y)
        # for i in range(1, 5):
        #     self.screen.print_at("│", x, y + i)
        # for i in range(1, 5):
        #     self.screen.print_at("│", x + 10, y + i)
        # self.screen.print_at("└─────────┘", x, y + 5)
        # self.screen.print_at(f"{tile.h}", x + 5, y + 1, colour=169)
        # self.screen.print_at(f"{tile.f}", x + 2, y + 2, colour=28)
        # self.screen.print_at(f"{tile.i}", x + 8, y + 2, colour=136)
        # self.screen.print_at(f"{tile.r}", x + 5, y + 3)
        # self.screen.print_at(f"{tile.g}", x + 2, y + 4, colour=226)
        # self.screen.print_at(f"{tile.s}", x + 8, y + 4, colour=21)


Screen.wrapper(Game)
