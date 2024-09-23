from typing import List, Tuple

def minesweeper_clicked(grid: List[List[int]], position: Tuple[int, int]) -> List[List[int]]:
    (x, y) = position
    (rows, cols) = (len(grid), len(grid[0]))
    if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == 0:
        return grid
    if grid[x][y] == 1:
        return grid
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(cols, y + 2)):
            if grid[i][j] != 1:
                grid[i][j] = 0
    return grid