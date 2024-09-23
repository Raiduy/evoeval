
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    min_path = [float('inf')] * k

    def dfs(i, j, path):
        nonlocal min_path
        if len(path) == k:
            min_path = min(min_path, path)
            return
        for (dx, dy) in directions:
            (x, y) = (i + dx, j + dy)
            if 0 <= x < n and 0 <= y < n:
                dfs(x, y, path + [grid[x][y]])
    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]])
    return min_path