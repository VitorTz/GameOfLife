from src.check_events import check_events
from src.constants import Constants
from src.globals import Globals
from src.evolve import evolve
from src.menu import Menu
import pygame


def main() -> None:
    pygame.init()
    Globals.display = pygame.display.set_mode(Constants.window_size)
    pygame.display.set_caption(Constants.window_title)
    Globals.reset_globals()
    
    menu = Menu()

    while True:
        Globals.display.fill(Constants.window_bg_color)
        Globals.window_frames += 1
        check_events(menu)
        evolve()
        menu.draw_menu()
        pygame.display.update()


if __name__ == "__main__":
    main()