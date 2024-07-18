def product_of_odd_prime_factors(n):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def next_prime(n):
        while True:
            n += 1
            if is_prime(n):
                return n
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor = next_prime(divisor)
    product = 1
    for factor in factors:
        if factor % 2 != 0:
            product *= factor
    return product if product != 1 else 0