from src.screenshot import take_screenshot
from src.constants import Constants
from src.globals import Globals
from src.image import Image
from sys import exit
import pygame



class Menu:

    """
        O menu é apenas uma imagem com informações 
        sobre o funcionamento do jogo.
    """
    
    __menu_img: Image  # Imagem que representa o menu
    __pattern_img: Image  # Imagem que diz para o usuário o número do padrão sendo exibido

    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self.__menu_img = Image(
            Constants.menu_image_path, Constants.menu_image_pos
        )
        self.__pattern_img = Image(
            Constants.patterns_image_path[Globals.pattern_id], Constants.pattern_image_pos
        )

    def draw_menu(self) -> None:
        if not Globals.is_running:
            self.__menu_img.draw()
            self.__pattern_img.draw()
    
    def check_events(self) -> None:
        """
            Responde as teclas pressionadas no teclado pelo usuário
        """
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == Constants.pause_key:
                    Globals.is_running = not Globals.is_running
                elif e.key == Constants.screenshot_key:
                    take_screenshot(Globals.generation)
                elif e.key == Constants.reset_key:
                    Globals.reset_globals()
                elif e.key in Globals.digits:
                    digit_pressed: int = Globals.digits[e.key]
                    Globals.pattern_id = digit_pressed
                    Globals.reset_globals()
                    self.reset()
