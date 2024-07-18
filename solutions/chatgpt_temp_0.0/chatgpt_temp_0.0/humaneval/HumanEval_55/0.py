

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Invalid input. n must be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib_prev = 1
        fib_curr = 1
        for _ in range(3, n+1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr
