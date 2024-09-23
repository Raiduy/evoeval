
def count_up_to(n):
    """Create a function that takes a non-negative integer n and returns a list of prime numbers less than n."""

    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, n) if is_prime(i)]
    return primes