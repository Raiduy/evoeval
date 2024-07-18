def spider_web_jump(arr):
    n = len(arr)
    m = len(arr[0])
    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + arr[i - 1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + arr[i][j - 1])
    return dp[n - 1][m - 1]