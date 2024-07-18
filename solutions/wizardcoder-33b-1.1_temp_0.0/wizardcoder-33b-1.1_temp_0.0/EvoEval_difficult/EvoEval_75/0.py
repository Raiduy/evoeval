def is_multiply_prime(a, b):
    primes = [i for i in range(2, a + 1) if is_prime(i)]
    factors = []
    for prime in primes:
        while a % prime == 0:
            factors.append(prime)
            a /= prime
    return (len(set(factors)) == b, sorted(list(set(factors))))