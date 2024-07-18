from typing import List


def factorize(n: int) -> List[int]:

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1
        while factor == 1:
            for count in range(cycle_size):
                if factor > 1:
                    break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)
            cycle_size *= 2
            x_fixed = x
        return factor

    def gcd(x, y):
        while y:
            (x, y) = (y, x % y)
        return x
    factors = []
    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next
    return sorted(factors, reverse=True)