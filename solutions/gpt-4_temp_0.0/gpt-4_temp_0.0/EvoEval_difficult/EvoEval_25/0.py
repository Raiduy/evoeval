from typing import List, Tuple

def factorize_and_count(n: int) -> List[Tuple[int, int]]:
    factors = []
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factors.append((2, count))
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
    if n > 2:
        factors.append((n, 1))
    return factors