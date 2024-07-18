
def skjkasdkd(lst):
    """Find the smallest prime in the list and return the sum of its digits."""
    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0
    smallest_prime = min(primes)
    return sum_of_digits(smallest_prime)