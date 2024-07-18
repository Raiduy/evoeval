from typing import List, Tuple

def find_subset_closest_elements(numbers: List[float], subset_size: int) -> Tuple[float, ...]:
    numbers.sort()
    min_diff = float('inf')
    min_subset = ()
    for i in range(len(numbers) - subset_size + 1):
        subset = numbers[i:i + subset_size]
        diff = subset[-1] - subset[0]
        if diff < min_diff:
            min_diff = diff
            min_subset = subset
        elif diff == min_diff:
            if sum(subset) < sum(min_subset):
                min_subset = subset
            elif sum(subset) == sum(min_subset):
                if subset[0] < min_subset[0]:
                    min_subset = subset
    return tuple(min_subset)