from typing import List, Tuple

def minesweeper_clicked(grid: List[List[int]], position: Tuple[int, int]) -> List[List[int]]:
    (x, y) = position
    if x < 0 or y < 0 or x >= len(grid) or (y >= len(grid[0])):
        return grid
    if grid[x][y] == 1:
        return grid
    if grid[x][y] == 0:
        return grid
    grid[x][y] = 0
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        (nx, ny) = (x + dx, y + dy)
        if nx >= 0 and ny >= 0 and (nx < len(grid)) and (ny < len(grid[0])) and (grid[nx][ny] != 1):
            minesweeper_clicked(grid, (nx, ny))
    return grid