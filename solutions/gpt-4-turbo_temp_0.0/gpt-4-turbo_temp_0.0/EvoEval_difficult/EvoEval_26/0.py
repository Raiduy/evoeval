from typing import List, Tuple


def remove_duplicates_and_count(numbers: List[int]) -> Tuple[List[int], List[int]]:
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    unique_numbers = []
    counts = []
    for num in numbers:
        if count_dict[num] == 1:
            unique_numbers.append(num)
            counts.append(count_dict[num])
    return (unique_numbers, counts)