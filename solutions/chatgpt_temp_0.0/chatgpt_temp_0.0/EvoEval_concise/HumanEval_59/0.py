

def largest_prime_factor(n: int):
    """Finds n's largest non-prime factor. Assumes n > 1 and n is non-prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n