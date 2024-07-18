

def skjkasdkd(lst):
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        """Return the sum of the digits of a number."""
        return sum(int(digit) for digit in str(n))

    # Find the largest prime number in the list
    largest_prime = None
    for number in lst:
        if is_prime(number) and (largest_prime is None or number > largest_prime):
            largest_prime = number

    # If there's no prime number in the list, return 0
    if largest_prime is None:
        return 0

    # Return the sum of the digits of the largest prime number
    return sum_of_digits(largest_prime)
