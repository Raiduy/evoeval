def product_of_odd_prime_factors(n):
    i = 2
    product = 1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i % 2 != 0:
                product *= i
    if n > 1 and n % 2 != 0:
        product *= n
    return product if product != 1 else 0