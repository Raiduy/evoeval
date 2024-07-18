
def smallest_prime_factor(n: int):
    """Return the smallest prime factor of n. Assume n > 1 and is not a prime."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n