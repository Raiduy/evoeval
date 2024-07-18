
def is_multiply_prime(a):
    """Returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    """
    def is_prime(n):
        """Returns true if the given number is prime, false otherwise."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            if is_prime(i):
                factors.append(i)
            if is_prime(a // i):
                factors.append(a // i)
    factors = list(set(factors))
    return len(factors) == 3 and all(is_prime(f) for f in factors)
