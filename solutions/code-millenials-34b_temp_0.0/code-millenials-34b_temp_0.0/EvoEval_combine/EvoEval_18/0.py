
def min_triplets_sum(nums):
    if len(nums) < 3:
        return 0
    min_sum = float('inf')
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                min_sum = min(min_sum, nums[i] + nums[j] + nums[k])
    return min_sum if min_sum != float('inf') else 0