from typing import List, Tuple

def minesweeper_clicked(grid: List[List[int]], position: Tuple[int, int]) -> List[List[int]]:
    (x, y) = position
    if x < 0 or y < 0 or x >= len(grid) or (y >= len(grid[0])):
        return grid
    if grid[x][y] == 1:
        return grid
    elif grid[x][y] == 0:
        return grid
    else:
        grid[x][y] = 0
        for i in range(max(0, x - 1), min(len(grid), x + 2)):
            for j in range(max(0, y - 1), min(len(grid[0]), y + 2)):
                if grid[i][j] == -1:
                    grid[i][j] = 0
        return grid