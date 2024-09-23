def is_multiply_prime(a, b):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    primes = []
    i = 2
    while a > 1:
        if a % i == 0 and is_prime(i):
            primes.append(i)
            a /= i
        else:
            i += 1
    if len(primes) == b:
        return (True, sorted(primes))
    else:
        return (False, [])