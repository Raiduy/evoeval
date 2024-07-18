def princess_rescue(coord, grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                continue
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    if dp[coord[0]][coord[1]] == float('inf'):
        return -1
    return dp[coord[0]][coord[1]]