from asciimatics.screen import Screen
from civ import Civilization



def main(screen):
    while True:
        screen.get_key()
        screen.refresh()

Screen.wrapper(main)
