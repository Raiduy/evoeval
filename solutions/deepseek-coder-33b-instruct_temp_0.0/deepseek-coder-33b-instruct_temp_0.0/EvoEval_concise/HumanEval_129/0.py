
def minPath(grid, k):
    N = len(grid)
    dp = [[[float('inf')] * (k + 1) for _ in range(N)] for _ in range(N)]
    path = [[[[]] * (k + 1) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j][1] = grid[i][j]
            path[i][j][1] = [grid[i][j]]
    for l in range(2, k + 1):
        for i in range(N):
            for j in range(N):
                for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < N and 0 <= y < N:
                        if dp[i][j][l] > dp[x][y][l - 1] + grid[i][j]:
                            dp[i][j][l] = dp[x][y][l - 1] + grid[i][j]
                            path[i][j][l] = path[x][y][l - 1] + [grid[i][j]]
    min_path = min((path[i][j][k] for i in range(N) for j in range(N)))
    return min_path