from typing import List, Tuple


def remove_duplicates_and_count(numbers: List[int]) -> Tuple[List[int], List[int]]:
    counts = {}
    unique_numbers = []
    unique_counts = []
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in numbers:
        if counts[num] == 1:
            unique_numbers.append(num)
            unique_counts.append(counts[num])
    return (unique_numbers, unique_counts)