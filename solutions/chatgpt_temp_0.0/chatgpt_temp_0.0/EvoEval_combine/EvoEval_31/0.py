
from typing import List

def special_prime_factorial(n: int) -> int:
    prime_factors = factorize(n)
    factorials = [factorial(factor) for factor in prime_factors]
    return product(factorials)