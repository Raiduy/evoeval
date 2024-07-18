
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    cur_sum = 0
    for num in nums:
        cur_sum = min(num, cur_sum + num)
        min_sum = min(min_sum, cur_sum)
    return min_sum
