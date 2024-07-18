
import math

def minSubArraySumEvenOdd(nums):
    min_sum = float('inf')
    even_count = 0
    odd_count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if current_sum < min_sum:
            min_sum = current_sum
    return (even_count, odd_count)