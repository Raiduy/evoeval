
import math

def minSubArraySumEvenOdd(nums):
    min_sum = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            min_sum = min(min_sum, sum(nums[i:j + 1]))
    even_count = sum((1 for digit in str(min_sum) if int(digit) % 2 == 0))
    odd_count = sum((1 for digit in str(min_sum) if int(digit) % 2 != 0))
    return (even_count, odd_count)