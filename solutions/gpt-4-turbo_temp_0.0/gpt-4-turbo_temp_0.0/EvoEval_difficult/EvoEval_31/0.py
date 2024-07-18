def is_prime_sum(lst, n):
    primes_up_to_n = generate_primes(n)
    for num in lst:
        if n - num in primes_up_to_n and num in primes_up_to_n:
            if n - num != num or lst.count(num) > 1:
                return True
    return False