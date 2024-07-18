
def minPath(grid, k):
    N = len(grid)
    dp = [[[float('inf')] * (k + 1) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j][0] = 0

    def dfs(x, y, k):
        if k == 0:
            return []
        if dp[x][y][k] != float('inf'):
            return dp[x][y][k]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                path = dfs(nx, ny, k - 1)
                if path is not None:
                    path = [grid[x][y]] + path
                    if len(path) <= k and (not dp[x][y][k] or path < dp[x][y][k]):
                        dp[x][y][k] = path
        return dp[x][y][k]

    for i in range(N):
        for j in range(N):
            dfs(i, j, k)

    return min(min(dp[i][j][k] for i in range(N) for j in range(N)) for k in range(1, k + 1))
