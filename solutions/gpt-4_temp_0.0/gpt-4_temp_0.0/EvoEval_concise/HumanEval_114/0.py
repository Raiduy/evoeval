import math

def minSubArraySum(nums):
    """
    Return the minimum sum of any non-empty sub-array from an array of integers.
    
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) returns 1
    minSubArraySum([-1, -2, -3]) returns -6
    """
    min_sum = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            min_sum = min(min_sum, sum(nums[i:j + 1]))
    return min_sum