
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
    primes = [n for n in numbers if is_prime(n)]
    return (sum(primes), 1 if not primes else prod(primes))