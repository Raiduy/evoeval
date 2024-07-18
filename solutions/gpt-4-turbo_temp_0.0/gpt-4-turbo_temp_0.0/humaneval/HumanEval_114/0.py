
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize current sum and minimum sum to the first element
    current_sum = min_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # If current sum is positive, it cannot contribute to the minimum sum, so start a new subarray from the current element
        # Else, add the current element to the current sum
        current_sum = min(num, current_sum + num)
        
        # Update the minimum sum if the current sum is smaller
        min_sum = min(min_sum, current_sum)
    
    return min_sum
