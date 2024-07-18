
def min_triplets_sum(nums: list):
    if len(nums) < 3:
        return 0
    min_sum = float('inf')
    for i in range(len(nums) - 2):
        curr_sum = sum(nums[i:i + 3])
        min_sum = min(min_sum, curr_sum)
    return min_sum