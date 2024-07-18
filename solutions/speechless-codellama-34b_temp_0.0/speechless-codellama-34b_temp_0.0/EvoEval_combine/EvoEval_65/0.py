
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
    power = 2 ** n % p
    largest_divisor = 1
    for i in range(2, p):
        if power % i == 0:
            largest_divisor = i
    return largest_divisor