
def smallest_prime_factor(n: int) -> int:
    """Return the smallest prime factor of n. Assume n > 1 and is not a prime.
    >>> smallest_prime_factor(13195)
    5
    >>> smallest_prime_factor(2048)
    2
    """
    for i in range(2, n + 1):
        if n % i == 0:
            return i
    return n