from src.globals import Globals
from src.image import Image
import pygame


class Notification:

    """
    Mostra uma notifição (em formato de imagem) para o usuário
    """

    def __init__(self, image: Image, total_frames: int = 5) -> None:
        self.__image = image
        self.__total_frames = Globals.window_frames + total_frames

    def __show_aux(self) -> None:
        while Globals.window_frames <= self.__total_frames:
            self.__image.draw()

    def show(self) -> None:
        pygame.threads.Thread(target=self.__show_aux).start()

