

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
        return 'Input should be a positive integer.'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)