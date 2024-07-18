def magical_staircase(n: int, magic_stones: list):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for stone in magic_stones:
            if i - stone >= 0:
                dp[i] += dp[i - stone]
    return dp[n]