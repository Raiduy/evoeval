def complexity_increased(lst, n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if not any((i > 0 for i in lst)):
        return -1
    primes = [i for i in lst if is_prime(i)]
    if not primes:
        return -1
    return sum((int(digit) ** n for prime in primes for digit in str(prime)))