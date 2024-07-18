

def largest_prime_factor(n: int):
    """Finds n's largest non-prime factor. Assumes n > 1 and n is non-prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(n - 1, 1, -1):
        if n % i == 0 and (not is_prime(i)):
            return i
    return None