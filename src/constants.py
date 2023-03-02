from src.numba_otimization import is_prime
from typing import Callable
from pathlib import Path
import pygame


class Colors:


    grey = (30, 34, 39)
    red = (226, 31, 44)


class Constants:


    # window
    window_width = 1280
    window_height = 720
    window_size = (window_width, window_height)
    window_title = "Game of Life"
    window_bg_color = Colors.grey

    # keys
    pause_key: int = pygame.K_SPACE
    reset_key: int = pygame.K_z
    screenshot_key: int = pygame.K_s
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

    # font
    font = Path("res/JetBrainsMono-Regular.ttf")

    # cell
    cell_size = 1
    cell_color = Colors.red
    cell_rect = pygame.Rect(0, 0, cell_size, cell_size)

    # grid
    grid_lines = window_height // cell_size
    grid_columns = window_width // cell_size
    
    # patterns
    patterns_by_id: dict[int, Callable] = {
        1: lambda i, j : int(i % 20 == 0 or j % 20 == 0),
        2: lambda i, j : int(i % 33 == 0 or j % 33 == 0),
        3: lambda i, j : int(i % 20 == 0),
        4: lambda i, j : int(i % 60 == 0 or j % 60 == 0),
        5: lambda i, j : int(is_prime(Constants.grid_columns * i + (j+1))),
        6: lambda i, j : int(is_prime(i + j)),
        7: lambda i, j : int(is_prime(i + j) or (i % 60 == 0 or j % 60 == 0)),
        8: lambda i, j : int((i % 33 == 0 or j % 33 == 0) or (i % 60 == 0 or j % 60 == 0)),
        9: lambda i, j : int((i % 33 == 0 or j % 33 == 0) or (i % 60 == 0 or j % 60 == 0) or (i % 20 == 0 or j % 20 == 0))
    }

    # save screenshot
    screenshot_dir = Path("screenshots")
    notification_screenshot_saved = Path("res/screenshot_saved.png")
    notification_screenshot_saved_pos = (515, 656)

    # images
    menu_image_path = Path("res/menu.png")
    patterns_image_path: dict[int, Path] = {
        i: Path(f"res/pattern-{i}.png") for i in range(1, 10)
    }

    # images positions
    menu_image_pos = (15, 15)
    pattern_image_pos = (32, 217)