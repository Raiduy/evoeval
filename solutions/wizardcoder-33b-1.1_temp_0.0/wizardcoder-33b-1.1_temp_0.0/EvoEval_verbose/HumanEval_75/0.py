
def is_multiply_prime(a):
    if a < 100:
        primes = [i for i in range(2, a) if is_prime(i)]
        for i in primes:
            for j in primes:
                for k in primes:
                    if i * j * k == a:
                        return True
        return False
    else:
        return 'Undefined'