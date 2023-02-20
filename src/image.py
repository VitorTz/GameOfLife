from src.globals import Globals
from pathlib import Path
import pygame


class Image:

    def __init__(self, image: pygame.Surface | Path, left_top: tuple[int, int]) -> None:
        self.__image = pygame.image.load(image)
        self.__rect = self.__image.get_rect()
        self.__rect.left, self.__rect.top = left_top
    
    def draw(self) -> None:
        Globals.display.blit(self.__image, self.__rect)
