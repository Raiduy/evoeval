
def is_multiply_prime(a):
    """Check if a number is a product of 3 prime numbers."""
    factors = prime_factors(a)
    return len(factors) == 3