
import math

def minSubArraySumEvenOdd(nums):
    min_sum = float('inf')
    even_count = 0
    odd_count = 0
    for i in range(len(nums)):
        sum_ = 0
        for j in range(i, len(nums)):
            sum_ += nums[j]
            if sum_ < min_sum:
                min_sum = sum_
                even_count = sum((1 for k in str(min_sum) if k.isdigit() and int(k) % 2 == 0))
                odd_count = sum((1 for k in str(min_sum) if k.isdigit() and int(k) % 2 != 0))
    return (even_count, odd_count)