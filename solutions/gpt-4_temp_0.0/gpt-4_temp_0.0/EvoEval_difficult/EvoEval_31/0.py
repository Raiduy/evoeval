def is_prime_sum(lst, n):
    primes = set()
    for num in lst:
        if is_prime(num):
            if n - num in primes:
                return True
            primes.add(num)
    return False