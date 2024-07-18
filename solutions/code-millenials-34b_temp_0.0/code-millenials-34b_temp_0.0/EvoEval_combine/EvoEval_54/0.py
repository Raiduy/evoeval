
import math

def max_sum_of_prime_subarray(nums):
    max_sum = 0
    current_sum = 0
    for num in nums:
        if is_prime(num):
            current_sum += num
            max_sum = max(max_sum, current_sum)
        else:
            current_sum = 0
    return max_sum