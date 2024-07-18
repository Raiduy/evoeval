

def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
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
    # Base case: 2^0 = 1
    if n == 0:
        return 1 % p
    # Recursive step: calculate 2^(n//2) modulo p
    half_mod = modp(n // 2, p)
    # If n is even, the result is (half_mod)^2 % p
    if n % 2 == 0:
        return (half_mod * half_mod) % p
    # If n is odd, the result is 2 * (half_mod)^2 % p
    else:
        return (2 * half_mod * half_mod) % p
