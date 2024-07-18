
from typing import List, Tuple

def primes_sum_product(numbers: List[int]) -> Tuple[int, int]:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for n in numbers if is_prime(n)]
    return (sum(primes), eval('*'.join((str(p) for p in primes))) if primes else 1)