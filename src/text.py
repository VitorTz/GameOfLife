from src.constants import Constants
import pygame


class Text:

    __font = "res/JetBrainsMono-Regular.ttf"

    def __init__(self, text: str, pos: tuple[int, int]) -> None:
        self.text = text
        self.rect = pos
    
    @property
    def text(self) -> pygame.Surface:
        return self.__text
    
    @text.setter
    def text(self, text: pygame.Surface | str):
        if isinstance(text, str):
            font = pygame.font.Font(
                self.__font,
                12
            )
            self.__text = font.render(text, True, Constants.cell_color)
        elif isinstance(text, pygame.Surface):
            self.__text = text
    
    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @rect.setter
    def rect(self, rect: pygame.Rect | tuple[int, int]):
        if isinstance(rect, tuple):
            self.__rect = self.text.get_rect()
            self.__rect.left, self.__rect.top = rect
        elif isinstance(rect, pygame.Rect):
            self.__rect = rect

    def draw(self, display: pygame.Surface) -> None:
        display.blit(self.text, self.rect)