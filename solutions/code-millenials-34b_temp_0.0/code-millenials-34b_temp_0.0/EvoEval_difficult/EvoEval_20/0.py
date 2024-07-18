from typing import List, Tuple

def find_subset_closest_elements(numbers: List[float], subset_size: int) -> Tuple[float, ...]:
    numbers.sort()
    min_distance = float('inf')
    best_subset = ()
    for i in range(len(numbers) - subset_size + 1):
        subset = tuple(numbers[i:i + subset_size])
        distance = subset[-1] - subset[0]
        if distance < min_distance or (distance == min_distance and sum(subset) < sum(best_subset)):
            min_distance = distance
            best_subset = subset
    return best_subset