from pygame import K_SPACE, K_z, Rect, K_s
from pathlib import Path
from src.colors import Colors
from typing import Callable


class Constants:


    # window
    window_width = 1280
    window_height = 720
    window_size = (window_width, window_height)
    window_title = "Game of Life"
    window_bg_color = Colors.grey


    # keys
    pause_key: int = K_SPACE
    reset_key: int = K_z
    screenshot_key: int = K_s

    # cell
    cell_size = 1
    cell_color = Colors.blue
    cell_rect = Rect(0, 0, cell_size, cell_size)

    # grid
    grid_lines = window_height // cell_size
    grid_columns = window_width // cell_size
    
    # patterns
    patterns_by_id: dict[int, Callable] = {
        0: lambda i, j : int(i % 20 == 0 or j % 20 == 0),
        1: lambda i, j : int(i % 33 == 0 or j % 33 == 0),
        2: lambda i, j : int(i % 42 == 0)
    }

    # save screenshot
    screenshot_dir = Path("screenshot")