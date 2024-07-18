
def modp(n: int, p: int, q: int) -> int:
    """Return 2^(n+q) modulo p (be aware of numerics).
    >>> modp(3, 5, 1)
    1
    >>> modp(1101, 101, 2)
    8
    >>> modp(0, 101, 1)
    2
    >>> modp(3, 11, 2)
    10
    >>> modp(100, 101, 1)
    2
    """
    return pow(2, n + q, p)