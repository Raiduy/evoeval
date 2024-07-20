
def modp_largest_divisor(n: int, p: int) -> int:
    """Return the largest number smaller than 'p' which divides (2^n modulo p) evenly. 
    If no such number exists, return 1.
    
    >>> modp_largest_divisor(3, 5)
    3
    >>> modp_largest_divisor(1101, 101)
    2
    >>> modp_largest_divisor(0, 101)
    1
    >>> modp_largest_divisor(3, 11)
    8
    """
    mod = pow(2, n, p)
    for i in range(p - 1, 0, -1):
        if mod % i == 0:
            return i
    return 1