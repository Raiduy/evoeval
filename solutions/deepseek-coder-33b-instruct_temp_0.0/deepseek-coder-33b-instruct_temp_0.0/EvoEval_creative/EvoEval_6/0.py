from typing import List, Tuple

def minesweeper_clicked(grid: List[List[int]], position: Tuple[int, int]) -> List[List[int]]:
    (x, y) = position
    if x < 0 or y < 0 or x >= len(grid) or (y >= len(grid[0])):
        return grid
    if grid[x][y] == 1:
        return grid
    if grid[x][y] == 0:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and j >= 0 and (i < len(grid)) and (j < len(grid[0])):
                    grid[i][j] = 0
    return grid