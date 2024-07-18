
def count_up_to(n):
    """Create a function that takes a non-negative integer n and returns a list of prime numbers less than n."""
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes