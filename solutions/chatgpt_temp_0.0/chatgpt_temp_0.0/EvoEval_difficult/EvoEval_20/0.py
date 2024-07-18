from typing import List, Tuple

def find_subset_closest_elements(numbers: List[float], subset_size: int) -> Tuple[float, ...]:
    numbers.sort()
    min_diff = float('inf')
    result_subset = None
    for i in range(len(numbers) - subset_size + 1):
        subset = numbers[i:i + subset_size]
        diff = subset[-1] - subset[0]
        if diff < min_diff or (diff == min_diff and sum(subset) < sum(result_subset)):
            min_diff = diff
            result_subset = subset
    return tuple(result_subset)