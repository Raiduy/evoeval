def spider_web_jump(arr):
    rows = len(arr)
    cols = len(arr[0])
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = 0
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + arr[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + arr[i][j])
    return dp[-1][-1]