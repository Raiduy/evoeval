

def largest_prime_factor(n: int):
    """Finds n's largest non-prime factor. Assumes n > 1 and n is non-prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n