

def skjkasdkd(lst):

    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        """Return the sum of the digits of a number."""
        return sum((int(digit) for digit in str(n)))
    primes = [num for num in lst if is_prime(num)]
    if primes:
        largest_prime = max(primes)
    else:
        return 0
    return sum_of_digits(largest_prime)