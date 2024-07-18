
def is_multiply_prime(a):
    """Check if a number is a product of 3 prime numbers.

    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = []
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            prime_factors.append(i)
    return len(prime_factors) == 3