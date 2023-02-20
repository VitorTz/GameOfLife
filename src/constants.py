from pygame import K_SPACE, K_z, Rect, K_s
from src.my_math import is_prime
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

    # font
    font = Path("res/JetBrainsMono-Regular.ttf")

    # cell
    cell_size = 1
    cell_color = Colors.blue
    cell_rect = Rect(0, 0, cell_size, cell_size)

    # grid
    grid_lines = window_height // cell_size
    grid_columns = window_width // cell_size
    
    # patterns
    patterns_by_id: dict[int, Callable] = {
        1: lambda i, j : int(i % 20 == 0 or j % 20 == 0),
        2: lambda i, j : int(i % 33 == 0 or j % 33 == 0),
        3: lambda i, j : int(i % 42 == 0),
        4: lambda i, j : int(i % 60 == 0 or j % 60 == 0),
        5: lambda i, j : int(is_prime(Constants.grid_columns * i + (j+1))),
        6: lambda i, j : int(0),
        7: lambda i, j : int(i % 42 == 0),
        8: lambda i, j : int(i % 42 == 0),
        9: lambda i, j : int(i % 42 == 0)
    }

    # save screenshot
    screenshot_dir = Path("screenshot")
    screenshot_saved_warning = Path("res/screenshot_saved.png")
    screenshot_saved_warning_pos = (515, 656)

    # images
    menu_image_path = Path("res/menu.png")
    patterns_image_path: dict[int, Path] = {
        i: Path(f"res/pattern-{i}.png") for i in range(1, 10)
    }

    # images positions
    menu_image_pos = (15, 15)
    pattern_image_pos = (32, 217)