def product_of_odd_prime_factors(n):
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
    odd_factors = [f for f in factors if f % 2 != 0]
    if odd_factors:
        return int(prod(odd_factors))
    else:
        return 0