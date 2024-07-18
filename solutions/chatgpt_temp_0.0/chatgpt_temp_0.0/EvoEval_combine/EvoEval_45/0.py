
from typing import List, Tuple

def primes_sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple consisting of a sum and a product of all the prime numbers in the list.
    Empty sum should be equal to 0 and empty product should be equal to 1. Non-prime numbers should be ignored.
    """
    prime_sum = 0
    prime_product = 1
    for num in numbers:
        if is_prime(num):
            prime_sum += num
            prime_product *= num
    return (prime_sum, prime_product)