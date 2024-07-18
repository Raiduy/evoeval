def largest_prime_factor(n: int, m: int):

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
            if n == 1:
                break
    if is_prime(m):
        return max(factors)
    else:
        return min(factors)