from typing import List, Tuple

def minesweeper_clicked(grid: List[List[int]], position: Tuple[int, int]) -> List[List[int]]:
    (rows, cols) = (len(grid), len(grid[0]))
    (x, y) = position
    if x < 0 or x >= rows or y < 0 or (y >= cols):
        return grid
    if grid[x][y] == 1 or grid[x][y] == 0:
        return grid

    def reveal(x, y):
        if 0 <= x < rows and 0 <= y < cols and (grid[x][y] == -1):
            grid[x][y] = 0
            if not any((grid[i][j] == 1 for i in range(max(0, x - 1), min(x + 2, rows)) for j in range(max(0, y - 1), min(y + 2, cols)))):
                for i in range(max(0, x - 1), min(x + 2, rows)):
                    for j in range(max(0, y - 1), min(y + 2, cols)):
                        reveal(i, j)
    reveal(x, y)
    return grid