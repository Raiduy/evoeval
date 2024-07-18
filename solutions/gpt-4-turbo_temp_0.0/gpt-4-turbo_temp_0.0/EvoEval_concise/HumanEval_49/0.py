

def modp(n: int, p: int) -> int:
    """
    Computes 2^n modulo p.
    
    Examples:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if n == 0:
        return 1
    half_power = modp(n // 2, p)
    if n % 2 == 0:
        return half_power * half_power % p
    else:
        return 2 * (half_power * half_power) % p % p