
def minSubArraySum(nums):
    n = len(nums)
    min_sum = float('inf')
    current_sum = 0
    for i in range(n):
        current_sum += nums[i]
        min_sum = min(min_sum, current_sum)
        if current_sum > 0:
            current_sum = 0
    return min_sum
