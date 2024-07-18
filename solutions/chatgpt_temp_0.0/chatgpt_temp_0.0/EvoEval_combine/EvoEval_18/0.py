
def min_triplets_sum(nums: list):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array of size three. 

    If no such sub-array exists, return 0. A sub-array is a contiguous part of an array.

    Examples:
    min_triplets_sum([2, 3, 4, 1, -7, 4]) == -2   # The sub-array is [1, -7, 4]
    min_triplets_sum([1, 2, 3, -6, 5, 1, 2]) == -1  # The sub-array is [2, 3, -6]
    min_triplets_sum([2, 3]) == 0   # No such sub-array exists
    min_triplets_sum([-1, -2, -3]) == -6   # The sub-array is [-1, -2, -3]
    """
    if len(nums) < 3:
        return 0
    min_sum = float('inf')
    for i in range(len(nums) - 2):
        sub_array = nums[i:i + 3]
        sub_sum = sum(sub_array)
        min_sum = min(min_sum, sub_sum)
    return min_sum