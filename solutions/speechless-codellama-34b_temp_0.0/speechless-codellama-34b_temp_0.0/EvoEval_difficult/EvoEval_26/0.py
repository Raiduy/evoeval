from typing import List, Tuple


def remove_duplicates_and_count(numbers: List[int]) -> Tuple[List[int], List[int]]:
    unique_numbers = []
    counts = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
            counts.append(numbers.count(number))
    return (unique_numbers, counts)