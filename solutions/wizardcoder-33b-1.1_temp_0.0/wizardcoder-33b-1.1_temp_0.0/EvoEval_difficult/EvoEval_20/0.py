from typing import List, Tuple

def find_subset_closest_elements(numbers: List[float], subset_size: int) -> Tuple[float, ...]:
    numbers.sort()
    min_diff = float('inf')
    min_sum = float('inf')
    min_first = float('inf')
    result = ()
    for i in range(len(numbers) - subset_size + 1):
        subset = numbers[i:i + subset_size]
        diff = subset[-1] - subset[0]
        sum_subset = sum(subset)
        if diff < min_diff or (diff == min_diff and sum_subset < min_sum) or (diff == min_diff and sum_subset == min_sum and (subset[0] < min_first)):
            min_diff = diff
            min_sum = sum_subset
            min_first = subset[0]
            result = tuple(subset)
    return result