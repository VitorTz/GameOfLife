from src.constants import Constants
from src.globals import Globals
from src.image import Image


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
    