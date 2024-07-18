

def fib(n: int) -> int:
    if n <= 0:
        raise ValueError('n must be a positive integer.')
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)