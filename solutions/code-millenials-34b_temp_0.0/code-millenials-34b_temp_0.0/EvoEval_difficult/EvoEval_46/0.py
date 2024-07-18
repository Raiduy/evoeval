def fib4_memo(n: int, m: int):
    if n < 0 or m > n:
        return 'Invalid input'
    fib_dict = {0: 0, 1: 0, 2: 2, 3: 0}
    for i in range(4, n + 1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2] + fib_dict[i - 3] + fib_dict[i - 4]
    return fib_dict[n - m]