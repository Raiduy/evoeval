def is_multiply_prime(a, b):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [i for i in range(2, a) if is_prime(i)]
    factors = []
    for prime in primes:
        while a % prime == 0:
            factors.append(prime)
            a /= prime
    return (len(factors) == b, factors if len(factors) == b else [])