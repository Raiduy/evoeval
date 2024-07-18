from typing import List, Tuple

def factorize_and_count(n: int) -> List[Tuple[int, int]]:
    primes = sieve_of_eratosthenes(int(math.sqrt(n)) + 1)
    factors = []
    for prime in primes:
        if prime * prime > n:
            break
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        if count > 0:
            factors.append((prime, count))
    if n != 1:
        factors.append((n, 1))
    return factors