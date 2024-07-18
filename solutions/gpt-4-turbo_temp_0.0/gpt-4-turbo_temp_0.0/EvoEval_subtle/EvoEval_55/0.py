
def fib(n: int) -> int:
    """Return (n+1)-th Fibonacci number.
    >>> fib(10)
    89
    >>> fib(1)
    1
    >>> fib(8)
    34
    """
    (a, b) = (0, 1)
    for _ in range(n):
        (a, b) = (b, a + b)
    return b