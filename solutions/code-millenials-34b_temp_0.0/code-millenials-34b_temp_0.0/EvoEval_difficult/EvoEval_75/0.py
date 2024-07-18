def is_multiply_prime(a, b):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, a + 1):
        if is_prime(i):
            primes.append(i)
    if len(primes) < b:
        return (False, [])
    factors = primes[:b]
    product = 1
    for factor in factors:
        product *= factor
    if product == a:
        return (True, factors)
    else:
        return (False, [])