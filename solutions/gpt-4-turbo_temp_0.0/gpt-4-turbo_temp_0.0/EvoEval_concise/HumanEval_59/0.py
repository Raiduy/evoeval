

def largest_prime_factor(n: int) -> int:
    """Finds n's largest prime factor. Assumes n > 1.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = -1
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
    if n > 2:
        largest_factor = n
    return largest_factor