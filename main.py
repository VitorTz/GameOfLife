from typing import Callable
from src.constants import Constants
from src.globals import Globals
from src.screenshot import take_screenshot
from sys import exit
from numba import njit
import numpy as np
import pygame



def reset() -> None:
    pattern: Callable = Constants.patterns_by_id[Globals.pattern_id]
    Globals.num_generations = 0
    Globals.is_running = False
    Globals.generation = np.array([[pattern(i, j) for j in range(Constants.grid_columns)] for i in range(Constants.grid_lines)])
    Globals.next_generation = np.array([[pattern(i, j) for j in range(Constants.grid_columns)] for i in range(Constants.grid_lines)])
    

def check_events() -> None:
    Globals.keys.clear()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == Constants.pause_key:
                Globals.is_running = not Globals.is_running
            elif e.key == Constants.screenshot_key:
                take_screenshot(Globals.generation)
            elif e.key == Constants.reset_key:
                reset()
                

@njit(fastmath=True)
def apply_rules(gen: list[list[int]], next: list[list[int]], lines: int, columns: int, is_running: bool) -> tuple[int, int]:
    """
        Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
        Any live cell with more than three live neighbours dies (referred to as overpopulation).
        Any live cell with two or three live neighbours lives, unchanged, to the next generation.
        Any dead cell with exactly three live neighbours comes to life.
    """
    live_cells: list[tuple[int, int]] = []
    for i, line in enumerate(gen):
        for j, cell in enumerate(line):
            
            if cell:
                live_cells.append((i, j))

            if is_running:
                alive_neighbors = 0
                pos = ((i,j+1), (i,j-1), (i-1,j), (i+1,j), (i+1,j+1), (i+1,j-1), (i-1,j-1), (i-1,j+1))
                for x, y in pos:
                    a = 0 <= x < lines
                    b = 0 <= y < columns
                    if a and b and gen[x][y]:
                        alive_neighbors += 1

                status = cell
                if status and alive_neighbors < 2 or status and alive_neighbors > 3:
                    status = 0
                elif not status and alive_neighbors == 3:
                    status = 1
                
                next[i][j] = status
    
    return live_cells
    

def draw_cells(alive_cell: list[tuple[int, int]]) -> None:
    size = Constants.cell_size
    for i, j in alive_cell:
        pygame.draw.rect(
            Globals.display, 
            Constants.cell_color,
            (size * j, size * i, size, size)
        )
    

def move_to_next_generation() -> None:
    if Globals.is_running:
        Globals.generation, Globals.next_generation = Globals.next_generation, Globals.generation


def count_generations() -> None:
    if Globals.is_running:
        Globals.num_generations += 1

def mainloop() -> None:
    check_events()
    alive_cells: list[tuple[int, int]] = apply_rules(
        Globals.generation,
        Globals.next_generation,
        Constants.grid_lines,
        Constants.grid_columns,
        Globals.is_running
    )
    draw_cells(alive_cells)
    count_generations()
    move_to_next_generation()


def init_game() -> None:
    pygame.init()
    pygame.font.init()
    Globals.display = pygame.display.set_mode(Constants.window_size)
    pygame.display.set_caption(Constants.window_title)
    reset()

def main() -> None:
    init_game()

    while True:
        Globals.display.fill(Constants.window_bg_color)
        mainloop()
        pygame.display.update()


if __name__ == "__main__":
    main()