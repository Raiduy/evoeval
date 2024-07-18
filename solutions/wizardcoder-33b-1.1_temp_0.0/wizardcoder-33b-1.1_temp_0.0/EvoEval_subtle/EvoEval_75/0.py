
def is_multiply_prime(a):
    if a < 100:
        primes = [i for i in range(2, a) if is_prime(i)]
        count = 0
        for prime in primes:
            if a % prime == 0:
                a /= prime
                count += 1
        if count == 4:
            return True
    return False