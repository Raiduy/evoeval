
import math

def max_sum_of_prime_subarray(nums):
    """
    Given an array of integers nums, find the maximum sum of any non-empty sub-array
    of prime nums. If no prime subarray exists, return 0.
    A prime number is a number that has exactly two distinct positive divisors: 1 and itself.
    You may assume that all numbers in the array are greater than 0.
    
    Example
    max_sum_of_prime_subarray([1, 2, 3, 4, 5, 6]) == 5  # The subarray [2, 3] is a subarray with primes, and it has the maximum sum, so their sum, 5, is returned
    max_sum_of_prime_subarray([4, 6, 8, 10]) == 0 # There are no primes in the list
    max_sum_of_prime_subarray([2, 3, 5, 7, 11, 13]) == 41 # All numbers in this list are primes, so their sum, 41, is returned
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    max_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j + 1]
            if any((is_prime(num) for num in subarray)):
                max_sum = max(max_sum, sum(subarray))
    return max_sum