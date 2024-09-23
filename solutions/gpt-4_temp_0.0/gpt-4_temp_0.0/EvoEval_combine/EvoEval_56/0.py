def product_of_odd_prime_factors(n):

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
    odd_prime_factors = set(filter(lambda x: x % 2 != 0, factors))
    if not odd_prime_factors:
        return 0
    product = 1
    for factor in odd_prime_factors:
        product *= factor
    return product