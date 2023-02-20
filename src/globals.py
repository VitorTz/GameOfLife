from typing import Callable
from src.constants import Constants
import numpy as np
import pygame


class Globals:


    # display (late init)
    display: pygame.Surface = None

    # keyboard
    digits: dict[int, int] = {
        pygame.K_1: 1,
        pygame.K_2: 2,
        pygame.K_3: 3,
        pygame.K_4: 4,
        pygame.K_5: 5,
        pygame.K_6: 6,
        pygame.K_7: 7,
        pygame.K_8: 8,
        pygame.K_9: 9,
    }

    # game status
    is_running = False
    window_frames: int = 0
    
    # generations
    generation: list[list[int]] = None
    next_generation: list[list[int]] = None

    # patterns
    pattern_id = 1

    @staticmethod
    def reset_globals() -> None:
        pattern: Callable = Constants.patterns_by_id[Globals.pattern_id]
        Globals.is_running = False
        Globals.generation = np.array([[pattern(i, j) for j in range(Constants.grid_columns)] for i in range(Constants.grid_lines)])
        Globals.next_generation = np.array([[pattern(i, j) for j in range(Constants.grid_columns)] for i in range(Constants.grid_lines)])

