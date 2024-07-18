def complexity_increased(lst, n):
    if not any((i > 0 for i in lst)):
        return -1
    primes = [i for i in lst if is_prime(i)]
    if not primes:
        return -1
    total = 0
    for prime in primes:
        for digit in str(prime):
            total += int(digit) ** n
    return total