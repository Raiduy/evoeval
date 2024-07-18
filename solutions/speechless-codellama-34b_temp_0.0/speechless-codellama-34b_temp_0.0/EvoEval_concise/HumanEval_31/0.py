

def is_prime(n):
    """
    Checks if the input number is prime.
    Returns true for prime numbers, false for non-prime numbers.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True