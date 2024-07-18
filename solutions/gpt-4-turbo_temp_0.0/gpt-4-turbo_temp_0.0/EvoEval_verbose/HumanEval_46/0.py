

def fib4(n: int) -> int:
    """
    Calculate the n-th term of the Fib4 sequence iteratively.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    (a, b, c, d) = (0, 0, 2, 0)
    for _ in range(4, n + 1):
        next_term = a + b + c + d
        (a, b, c, d) = (b, c, d, next_term)
    return d