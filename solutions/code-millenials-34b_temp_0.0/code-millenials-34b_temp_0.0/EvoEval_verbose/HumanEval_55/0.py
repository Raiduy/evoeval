

def fib(n: int):
    if n <= 0:
        raise ValueError('Input should be a positive integer.')
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        (a, b) = (1, 1)
        for _ in range(n - 2):
            (a, b) = (b, a + b)
        return b