def smallest_change(arr, k):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for m in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
            if (prefix_sum[j + 1] - prefix_sum[i]) % k == 0:
                dp[i][j] = min(dp[i][j], dp[i + 1][j - 1] + 1)
    return dp[0][n - 1]