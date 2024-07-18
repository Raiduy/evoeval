
def min_triplets_sum(nums: list):
    n = len(nums)
    if n < 3:
        return 0
    min_sum = float('inf')
    for i in range(n - 2):
        (left, right) = (i + 1, n - 1)
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            min_sum = min(min_sum, current_sum)
            if current_sum < 0:
                left += 1
            else:
                right -= 1
    return min_sum if min_sum != float('inf') else 0