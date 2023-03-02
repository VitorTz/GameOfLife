from numba import njit


@njit(fastmath=True)
def apply_rules(
    gen: list[tuple[int, int]], 
    next: list[tuple[int, int]], 
    grid_lines: int, 
    grid_columns: int,
    is_running: bool
) -> list[tuple[int, int]]:
    """
        1 - Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
        2 - Any live cell with more than three live neighbours dies (referred to as overpopulation).
        3 - Any live cell with two or three live neighbours lives, unchanged, to the next generation.
        4 - Any dead cell with exactly three live neighbours comes to life.
    """
    alive_cells = []
    for i, line in enumerate(gen):
        for j, cell in enumerate(line):
            
            if cell:
                alive_cells.append((i, j))

            if is_running:
                # count neighbors
                neighbors = 0
                pos = ((i,j+1), (i,j-1), (i-1,j), (i+1,j), (i+1,j+1), (i+1,j-1), (i-1,j-1), (i-1,j+1))
                for x, y in pos:
                    a = 0 <= x < grid_lines
                    b = 0 <= y < grid_columns
                    if a and b and gen[x][y]:
                        neighbors += 1

                # Aplica as regras do jogo para a célula atual
                if cell:
                    next[i][j] = neighbors == 2 or neighbors == 3
                else:
                    next[i][j] = neighbors == 3
    return alive_cells


@njit(fastmath=True)
def is_prime(n: int) -> bool:
    """Retorna True se n for primo, falso caso contrário."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    for i in range(5, r+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
