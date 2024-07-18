def fib4_memo(n: int, m: int):
    if n < 0 or m > n:
        return 'Invalid input'
    fib4 = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])
    return fib4[-m]