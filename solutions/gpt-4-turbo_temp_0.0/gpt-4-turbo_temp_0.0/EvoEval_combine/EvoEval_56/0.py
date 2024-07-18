def product_of_odd_prime_factors(n):
    """Given a positive integer n, return the product of its unique odd prime factors.
    If all prime factors are even, return 0.
    Assume n > 1 and is not a prime.
    For example:
    product_of_odd_prime_factors(9) == 3
    product_of_odd_prime_factors(15) == 15
    product_of_odd_prime_factors(20) == 5
    product_of_odd_prime_factors(32) == 0
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    product = 1
    found_odd_prime = False
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            if i % 2 != 0:
                found_odd_prime = True
                product *= i
    return product if found_odd_prime else 0