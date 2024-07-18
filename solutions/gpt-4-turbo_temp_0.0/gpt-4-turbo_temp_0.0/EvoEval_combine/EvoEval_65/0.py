
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
    mod_result = pow(2, n, p)
    if mod_result <= 1:
        return 1
    for divisor in range(p - 1, 1, -1):
        if mod_result % divisor == 0:
            return divisor
    return 1