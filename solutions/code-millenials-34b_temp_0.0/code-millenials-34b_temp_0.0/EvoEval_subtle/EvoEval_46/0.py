
def fib4(n: int):
    if n < 2:
        return '0'
    elif n == 2:
        return '2'
    elif n == 3:
        return '0'
    else:
        fib = [0, 0, 2, 0] + [0] * (n - 3)
        for i in range(4, n + 1):
            fib[i] = int(fib[i - 1]) + int(fib[i - 2]) + int(fib[i - 3]) + int(fib[i - 4])
        return str(fib[n])