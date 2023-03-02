from typing import Callable
from src.constants import Constants
import numpy as np
import pygame


class Globals:


    # display (late init)
    display: pygame.Surface = None

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

