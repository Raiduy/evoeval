from typing import List, Tuple


def remove_duplicates_and_count(numbers: List[int]) -> Tuple[List[int], List[int]]:
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    unique_numbers = [num for num in numbers if counts[num] == 1]
    unique_counts = [counts[num] for num in unique_numbers]
    return (unique_numbers, unique_counts)