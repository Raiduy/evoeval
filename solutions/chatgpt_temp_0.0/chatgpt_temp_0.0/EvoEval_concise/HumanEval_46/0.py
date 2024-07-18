

def fib4(n: int):
    """Calculates the n-th element of the Fib4 sequence, defined as:
    fib4(n) -> 0 for n in {0, 1, 3}, 2 for n = 2, and fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n > 3.
    Uses an efficient non-recursive approach.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2
    else:
        fib = [0, 0, 2, 0]
        for i in range(4, n + 1):
            fib[i % 4] = fib[(i - 1) % 4] + fib[(i - 2) % 4] + fib[(i - 3) % 4] + fib[(i - 4) % 4]
        return fib[n % 4]