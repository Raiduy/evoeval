
def is_multiply_prime(a):
    """Check if a number is a product of 3 prime numbers."""
    factors = []
    for i in range(2, a + 1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
    return len(factors) == 3