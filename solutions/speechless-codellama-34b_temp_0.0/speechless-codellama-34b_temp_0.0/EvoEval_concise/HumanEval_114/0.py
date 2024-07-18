import math

def minSubArraySum(nums):
    """
    Return the minimum sum of any non-empty sub-array from an array of integers.
    
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) returns 1
    minSubArraySum([-1, -2, -3]) returns -6
    """
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
    return min_sum