
from typing import List, Tuple

def primes_sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the prime numbers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1. Non-prime numbers should be ignored.
    """
    sum_primes = 0
    product_primes = 1
    for num in numbers:
        if is_prime(num):
            sum_primes += num
            product_primes *= num
    return (sum_primes, product_primes)