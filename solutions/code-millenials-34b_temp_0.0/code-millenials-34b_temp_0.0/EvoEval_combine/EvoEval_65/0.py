
def modp_largest_divisor(n: int, p: int) -> int:
    """Return the largest number smaller than 'p' which divides (2^n modulo p) evenly. 
    If no such number exists, return 1.
    """
    mod_result = pow(2, n, p)
    largest_divisor = p - 1
    while largest_divisor > 1:
        if mod_result % largest_divisor == 0:
            return largest_divisor
        largest_divisor -= 1
    return 1