def is_prime_sum(lst, n):
    primes = [x for x in lst if is_prime(x)]
    prime_set = set(primes)
    for x in primes:
        if n - x in prime_set:
            return True
    return False