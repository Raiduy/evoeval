
def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than or equal to n. Return the list in descending order."""
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return primes[::-1]