
def smallest_prime_factor(n):
    """Return the smallest prime factor of n. Assume n > 1 and is not a prime."""
    assert n > 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i:
            continue
        return i
    return n