from typing import List, Tuple

def minesweeper_clicked(grid: List[List[int]], position: Tuple[int, int]) -> List[List[int]]:
    (x, y) = position
    (rows, cols) = (len(grid), len(grid[0]))
    if x < 0 or x >= rows or y < 0 or (y >= cols) or (grid[x][y] == 1):
        return grid
    if grid[x][y] == 0:
        return grid

    def is_valid_cell(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def reveal_adjacent_cells(i, j):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                (new_x, new_y) = (i + dx, j + dy)
                if is_valid_cell(new_x, new_y) and grid[new_x][new_y] != 1:
                    grid[new_x][new_y] = 0
                    if grid[new_x][new_y] == 0:
                        reveal_adjacent_cells(new_x, new_y)
    grid[x][y] = 0
    reveal_adjacent_cells(x, y)
    return grid