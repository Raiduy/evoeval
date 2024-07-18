
from typing import List, Tuple

def primes_sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the prime numbers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1. Non-prime numbers should be ignored.
    >>> primes_sum_product([])
    (0, 1)
    >>> primes_sum_product([1, 2, 3, 4])
    (5, 6)
    >>> primes_sum_product([5, 6, 7, 101, 11])
    (124, 38885)
    """

    def is_prime(n: int) -> bool:
        """ Check if a number is prime. """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_sum = 0
    prime_product = 1
    for num in numbers:
        if is_prime(num):
            prime_sum += num
            prime_product *= num
    return (prime_sum, prime_product)