

def largest_divisor(n: int) -> int:
    """Find the largest number smaller than n which divides n evenly.
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1