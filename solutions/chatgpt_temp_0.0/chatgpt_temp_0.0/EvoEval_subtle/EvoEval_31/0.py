

def is_prime(n):
    """Return true if a given number is prime, and false otherwise. If the number is less than 2, return 'Invalid Input'."""
    if n < 2:
        return 'Invalid Input'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True