from src.constants import Constants
from src.globals import Globals
from src import game_of_live
from src.menu import Menu
import pygame


def init_game() -> None:            
    pygame.init()
    pygame.font.init()
    Globals.display = pygame.display.set_mode(Constants.window_size)
    pygame.display.set_caption(Constants.window_title)
    Globals.reset_globals()


def main() -> None:
    init_game()
    menu = Menu()

    while True:
        Globals.display.fill(Constants.window_bg_color)
        Globals.window_frames += 1
        menu.check_events()
        game_of_live.evolve()
        menu.draw_menu_img()
        pygame.display.update()


if __name__ == "__main__":
    main()