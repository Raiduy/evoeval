

def modp(n: int, p: int) -> int:
    """
    This function calculates the modulus of the power of 2 raised to a given integer, n, by another given integer, p. 
    The operation performed is 2^n modulo p. This function can be used for calculations involving large powers and moduli,
    but it's important to keep numerical stability in mind.

    Parameters:
    n (int): This is the exponent to which 2 is raised. This must be a non-negative integer.
    p (int): This is the modulus. It must be a positive integer.

    Returns:
    int: The result of the operation 2^n modulo p is returned as an integer.

    Examples:
    >>> modp(3, 5)
    3
    The above example returns 3 because 2^3 = 8, and 8 modulo 5 equals 3.

    >>> modp(1101, 101)
    2
    This is a case with larger numbers. It returns 2 because 2^1101 modulo 101 equals 2.

    >>> modp(0, 101)
    1
    This returns 1 because 2^0 = 1, and 1 modulo any number equals 1.

    >>> modp(3, 11)
    8
    This returns 8 because 2^3 = 8, and 8 modulo 11 equals 8 (as 11 > 8).

    >>> modp(100, 101)
    1
    This returns 1 because 2^100 modulo 101 equals 1.
    """
    return pow(2, n, p)