def is_multiply_prime(a, b):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, a) if is_prime(i)]
    result = []
    for i in range(2, len(primes) + 1):
        for prime_nums in itertools.combinations(primes, i):
            if a == np.prod(prime_nums) and len(prime_nums) == b:
                result = list(prime_nums)
                break
    return (len(result) == b, sorted(result))