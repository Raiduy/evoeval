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
    factors = []
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] * primes[j] == a:
                factors.append(primes[i])
                factors.append(primes[j])
                break
    if len(factors) == b:
        return (True, sorted(factors))
    else:
        return (False, [])