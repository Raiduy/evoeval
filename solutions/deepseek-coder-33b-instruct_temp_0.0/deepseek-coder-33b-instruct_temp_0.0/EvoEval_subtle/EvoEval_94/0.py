
def skjkasdkd(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    primes = [i for i in lst if is_prime(i)]
    if not primes:
        return 0
    smallest_prime = min(primes)
    return sum((int(digit) for digit in str(smallest_prime)))