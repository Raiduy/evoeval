def is_multiply_prime(a, b):
    """Check if a is the multiplication of exactly b prime numbers."""
    factors = prime_factors(a)
    if len(factors) == b:
        return (True, sorted(factors))
    else:
        return (False, [])