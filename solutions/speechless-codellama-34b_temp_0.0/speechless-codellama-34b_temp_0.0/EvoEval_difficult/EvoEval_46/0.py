def fib4_memo(n: int, m: int):
    if n < 0 or m > n:
        return 'Invalid input'
    memo = {}
    for i in range(n + 1):
        if i == 0:
            memo[i] = 0
        elif i == 1:
            memo[i] = 0
        elif i == 2:
            memo[i] = 2
        elif i == 3:
            memo[i] = 0
        else:
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3] + memo[i - 4]
    return memo[n - m + 1]