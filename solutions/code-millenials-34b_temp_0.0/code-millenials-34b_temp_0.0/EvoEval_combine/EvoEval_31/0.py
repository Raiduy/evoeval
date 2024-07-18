
from typing import List

def special_prime_factorial(n: int) -> int:
    factors = prime_factors(n)
    product = 1
    for factor in set(factors):
        count = factors.count(factor)
        product *= factorial(factor) ** count
    return product