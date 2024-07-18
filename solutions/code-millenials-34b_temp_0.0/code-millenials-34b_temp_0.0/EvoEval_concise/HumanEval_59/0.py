

def largest_prime_factor(n: int):
    """Finds n's largest non-prime factor. Assumes n > 1 and n is non-prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n