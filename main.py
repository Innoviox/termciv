from asciimatics.screen import Screen
from civ import Civilization
from map import Map

def main(screen):
    m = Map()

    while True:
        screen.print_at(m.at(0, 0), 0, 0)
        # screen.get_key()

        screen.refresh()

Screen.wrapper(main)
