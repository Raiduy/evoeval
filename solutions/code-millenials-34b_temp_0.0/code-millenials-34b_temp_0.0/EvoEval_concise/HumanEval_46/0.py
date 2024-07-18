

def fib4(n: int):
    if n in {0, 1, 3}:
        return 0
    elif n == 2:
        return 2
    else:
        fib = [0, 0, 2, 0] + [0] * (n - 3)
        for i in range(4, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4]
        return fib[n]