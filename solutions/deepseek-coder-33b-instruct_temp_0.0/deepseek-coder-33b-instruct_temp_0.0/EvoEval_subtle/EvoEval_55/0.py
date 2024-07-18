
def fib(n: int):
    """Return (n+1)-th Fibonacci number.
    >>> fib(10)
    89
    >>> fib(1)
    1
    >>> fib(8)
    34
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        (a, b) = (0, 1)
        for _ in range(n - 1):
            (a, b) = (b, a + b)
        return b