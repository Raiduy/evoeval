import math

def minSubArraySum(nums):
    """
    This function, minSubArraySum, takes an array of integers as its input and calculates the minimum sum that can be obtained from any non-empty sub-array within the input array. 

    A sub-array is defined as a contiguous portion of the array, which can range in size from a single element to the entire array. The sum of a sub-array is calculated as the total of all the integers within that sub-array. 

    The goal of the function is to determine the smallest possible sum that can be achieved from any of these sub-arrays. In the case of an array that contains both positive and negative numbers, the smallest sum could be a negative number. 

    The function returns this minimum sum as an integer. 

    Parameters:
    nums (List[int]): An array of integers. This array can contain both positive and negative numbers, and has a length ranging from 1 to len(nums).

    Returns:
    int: The minimum sum that can be obtained from any non-empty sub-array within the input array, nums.

    Examples:
    minSubArraySum([2, 3, 4, 1, 2, 4]) returns 1, because the sub-array with the smallest sum is [1], which sums to 1.
    minSubArraySum([-1, -2, -3]) returns -6, because the sub-array with the smallest sum is [-1, -2, -3], which sums to -6.
    """
    if not nums:
        return 0
    current_sum = nums[0]
    min_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = min(nums[i], current_sum + nums[i])
        min_sum = min(min_sum, current_sum)
    return min_sum