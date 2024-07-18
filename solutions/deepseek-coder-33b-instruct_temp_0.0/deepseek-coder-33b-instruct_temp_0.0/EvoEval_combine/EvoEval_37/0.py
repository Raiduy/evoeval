
import math

def minSubArraySumEvenOdd(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums. Then, return a tuple that has the number of even and odd digits in 
    this minimum sum respectively.

    Example:
    minSubArraySumEvenOdd([2, 3, 4, 1, 2, 4]) == (0, 1)  # minimum sum is 1 which has 0 even digit and 1 odd digit
    minSubArraySumEvenOdd([-1, -2, -3]) == (1, 0)  # minimum sum is -6 which has 1 even digit and 0 odd digit
    """
    min_sum = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            min_sum = min(min_sum, sum(nums[i:j + 1]))
    even_count = 0
    odd_count = 0
    for digit in str(abs(min_sum)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)