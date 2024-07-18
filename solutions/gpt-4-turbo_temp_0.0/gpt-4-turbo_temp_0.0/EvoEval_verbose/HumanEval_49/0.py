

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
    """
    result = 1
    base = 2
    base = base % p
    while n > 0:
        if n % 2 == 1:
            result = result * base % p
        n = n // 2
        base = base * base % p
    return result