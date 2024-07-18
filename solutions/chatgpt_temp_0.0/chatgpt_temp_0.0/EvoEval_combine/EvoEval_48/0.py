
from typing import List

def prime_prefixed_strings(strings: List[str], prefix: str) -> List[str]:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [s for s in strings if s.startswith(prefix) and is_prime(len(s))]