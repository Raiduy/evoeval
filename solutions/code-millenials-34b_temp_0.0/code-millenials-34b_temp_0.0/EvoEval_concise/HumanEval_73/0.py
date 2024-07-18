
def smallest_change(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            if gap == 0:
                dp[i][j] = 0
            elif gap == 1:
                dp[i][j] = 0 if arr[i] == arr[j] else 1
            elif arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
    return dp[0][n - 1]