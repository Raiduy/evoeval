import math

def minSubArraySum(nums):
    """
    Return the minimum sum of any non-empty sub-array from an array of integers.
    
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) returns 1
    minSubArraySum([-1, -2, -3]) returns -6
    """
    min_sum = math.inf
    cur_sum = 0
    for num in nums:
        cur_sum = min(num, cur_sum + num)
        min_sum = min(min_sum, cur_sum)
    return min_sum