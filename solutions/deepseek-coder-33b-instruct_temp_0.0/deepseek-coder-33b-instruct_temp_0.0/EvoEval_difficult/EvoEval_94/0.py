def complexity_increased(lst, n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_digits(num):
        return sum((int(digit) ** n for digit in str(num)))
    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return -1
    return sum((sum_of_digits(prime) for prime in primes))