def complexity_increased(lst, n):
    if not any((x > 0 for x in lst)):
        return -1
    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return -1
    sum = 0
    for prime in primes:
        digits = [int(d) for d in str(prime)]
        for i in range(n):
            sum += digits[i] ** n
    return sum