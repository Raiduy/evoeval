
from typing import List

def special_prime_factorial(n: int) -> int:

    def factorize(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    factors = factorize(n)
    result = 1
    for factor in factors:
        result *= factorial(factor)
    return result