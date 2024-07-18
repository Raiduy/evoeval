from typing import List, Tuple

def factorize_and_count(n: int) -> List[Tuple[int, int]]:

    def prime_factors(n):
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
    factors = prime_factors(n)
    factor_counts = [(factor, factors.count(factor)) for factor in set(factors)]
    return sorted(factor_counts)