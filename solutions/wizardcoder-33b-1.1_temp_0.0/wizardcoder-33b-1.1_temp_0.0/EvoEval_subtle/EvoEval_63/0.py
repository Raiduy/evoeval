
def fibfib(n: int, memo={0: 0, 1: 0, 2: 1}):
    if n not in memo:
        memo[n] = fibfib(n - 3, memo) + fibfib(n - 2, memo) - fibfib(n - 1, memo)
    return memo[n]