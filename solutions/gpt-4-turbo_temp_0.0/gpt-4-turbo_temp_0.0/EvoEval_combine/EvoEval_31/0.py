
from typing import List

def special_prime_factorial(n: int) -> int:
    """
    This function first factorizes the input 'n' into its prime factors and then calculates a special factorial.
    The 'special factorial' is defined as the product of factorials of all the prime factors of 'n'.
    The factors should be calculated number of times corresponding to how many times they appear in the factorization.
    The function should return the product of these factorials.
    """
    factors = prime_factors(n)
    result = 1
    for factor in factors:
        result *= factorial(factor)
    return result