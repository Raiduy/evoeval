def product_of_odd_prime_factors(n):
    """Given a positive integer n, return the product of its unique odd prime factors.
    If all prime factors are even, return 0.
    Assume n > 1 and is not a prime.
    For example:
    product_of_odd_prime_factors(9) == 3
    product_of_odd_prime_factors(15) == 15
    product_of_odd_prime_factors(20) == 5
    product_of_odd_prime_factors(32) == 0
    """
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    odd_prime_factors = [factor for factor in factors if factor % 2 != 0 and all((factor % j != 0 for j in range(2, int(factor ** 0.5) + 1)))]
    if all((factor % 2 == 0 for factor in factors)):
        return 0
    else:
        return 1 if len(odd_prime_factors) == 0 else reduce(lambda x, y: x * y, odd_prime_factors)