
def skjkasdkd(lst):
    primes = [i for i in lst if is_prime(i)]
    if not primes:
        return 0
    smallest_prime = min(primes)
    return sum((int(digit) for digit in str(smallest_prime)))