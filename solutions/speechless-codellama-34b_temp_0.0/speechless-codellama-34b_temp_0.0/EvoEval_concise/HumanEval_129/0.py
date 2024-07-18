
def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    path = []
    min_path = []

    def dfs(i, j, k, path):
        if k == 0:
            if path < min_path or not min_path:
                min_path.clear()
                min_path.extend(path)
            return
        visited[i][j] = True
        path.append(grid[i][j])
        for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            (x, y) = (i + dx, j + dy)
            if 0 <= x < n and 0 <= y < n and (not visited[x][y]):
                dfs(x, y, k - 1, path)
        visited[i][j] = False
        path.pop()
    for i in range(n):
        for j in range(n):
            dfs(i, j, k - 1, path)
    return min_path