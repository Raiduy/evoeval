
def minPath(grid, k):
    N = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    paths = []

    def dfs(i, j, path):
        if len(path) == k:
            paths.append(path)
            return
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                dfs(ni, nj, path + [grid[ni][nj]])

    for i in range(N):
        for j in range(N):
            dfs(i, j, [grid[i][j]])

    return min(paths)
