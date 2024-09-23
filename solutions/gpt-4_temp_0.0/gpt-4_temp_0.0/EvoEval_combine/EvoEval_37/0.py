
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
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            min_sum = min(min_sum, current_sum)
    min_sum = abs(min_sum)
    even_count = len([digit for digit in str(min_sum) if int(digit) % 2 == 0])
    odd_count = len([digit for digit in str(min_sum) if int(digit) % 2 != 0])
    return (even_count, odd_count)