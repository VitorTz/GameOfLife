from src.constants import Constants
from src.globals import Globals
from src.numba_otimization import apply_rules
import pygame

LiveCells = list[tuple[int, int]]

def draw_cells(live_cells: LiveCells) -> None:
    size = Constants.cell_size
    display: pygame.Surface = Globals.display
    color: tuple[int, int, int] = Constants.cell_color
    for i, j in live_cells:
        pygame.draw.rect(
            display, 
            color,
            (size * j, size * i, size, size)
        )


def move_to_next_generation() -> None:
    if Globals.is_running:
        Globals.generation, Globals.next_generation = Globals.next_generation, Globals.generation


def evolve() -> None:
    alive_cells = apply_rules(
        Globals.generation,
        Globals.next_generation,
        Constants.grid_lines,
        Constants.grid_columns,
        Globals.is_running
    )
    draw_cells(alive_cells)
    move_to_next_generation()
