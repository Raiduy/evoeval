import math

def minSubArraySum(nums):
    min_sum = math.inf
    current_sum = 0
    for num in nums:
        if current_sum > 0:
            current_sum = num
        else:
            current_sum += num
        min_sum = min(min_sum, current_sum)
    return min_sum