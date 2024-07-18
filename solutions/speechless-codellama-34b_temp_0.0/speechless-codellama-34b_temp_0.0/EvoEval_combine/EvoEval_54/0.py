
import math

def max_sum_of_prime_subarray(nums):
    max_sum = 0
    current_sum = 0
    start = 0
    for end in range(len(nums)):
        if is_prime(nums[end]):
            current_sum += nums[end]
        else:
            if current_sum > max_sum:
                max_sum = current_sum
                start = end
            current_sum = 0
    if current_sum > max_sum:
        max_sum = current_sum
    return max_sum