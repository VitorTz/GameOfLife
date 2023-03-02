from src.screenshot import take_screenshot
from src.constants import Constants
from src.globals import Globals
from src.menu import Menu
import pygame

def change_pattern(menu: Menu, pattern_num: int) -> None:
    Globals.pattern_id = pattern_num
    Globals.reset_globals()
    menu.reset()


def change_game_status() -> None:
    Globals.is_running = not Globals.is_running


def handle_keyboard(menu: Menu, key: int) -> None:
    if key in Constants.digits:
        return change_pattern(menu, Constants.digits[key])
    func = {
        Constants.pause_key: lambda : change_game_status(),
        Constants.screenshot_key: lambda : take_screenshot(Globals.generation),
        Constants.reset_key: lambda : Globals.reset_globals()
    }.get(key)
    if func: func()


def check_events(menu: Menu) -> None:
    """Responde as teclas pressionadas no teclado pelo usuário"""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif e.type == pygame.KEYDOWN:
            handle_keyboard(menu, e.key)
            
