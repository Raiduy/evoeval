from typing import List, Tuple


def sort_numbers(numbers: str, order: List[str]) -> str:
    num_list = numbers.split()
    sorted_list = []
    remaining_list = [num for num in num_list if num not in order]
    for num in order:
        sorted_list.extend([x for x in num_list if x == num])
    sorted_list.extend(remaining_list)
    return ' '.join(sorted_list)