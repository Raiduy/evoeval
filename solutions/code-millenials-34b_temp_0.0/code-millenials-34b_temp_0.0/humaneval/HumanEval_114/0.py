
def minSubArraySum(nums):
    current_sum = min_sum = sum(nums)
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum
