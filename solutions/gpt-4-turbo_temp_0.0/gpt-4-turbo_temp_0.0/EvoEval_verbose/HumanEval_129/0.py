
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    min_path = [float('inf')] * k

    def dfs(x, y, path, steps):
        if steps == k:
            nonlocal min_path
            min_path = min(min_path, path.copy())
            return
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n:
                path.append(grid[nx][ny])
                dfs(nx, ny, path, steps + 1)
                path.pop()
    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]], 1)
    return min_path