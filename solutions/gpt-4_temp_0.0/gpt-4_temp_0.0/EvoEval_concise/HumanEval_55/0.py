

def fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number.
    :param n: Index of the Fibonacci sequence.
    :return: The n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return 'Input should be positive integer'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        (a, b) = (0, 1)
        for _ in range(2, n):
            (a, b) = (b, a + b)
        return b