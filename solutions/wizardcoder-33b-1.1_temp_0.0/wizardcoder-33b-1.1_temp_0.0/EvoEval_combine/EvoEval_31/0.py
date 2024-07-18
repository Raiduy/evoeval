
from typing import List

def special_prime_factorial(n: int) -> int:

    def get_prime_factors(n: int) -> List[int]:
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    prime_factors = get_prime_factors(n)
    special_factorial = 1
    for factor in set(prime_factors):
        special_factorial *= factorial(prime_factors.count(factor)) * factorial(factor)
    return special_factorial