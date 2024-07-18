

def is_prime(n):
    """Return true if a given number is prime, and false otherwise. If the number is less than 2, return 'Invalid Input'.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    'Invalid Input'
    """
    if n < 2:
        return 'Invalid Input'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True