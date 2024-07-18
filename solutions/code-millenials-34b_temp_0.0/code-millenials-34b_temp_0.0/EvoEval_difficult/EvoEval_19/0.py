from typing import List, Tuple


def sort_numbers(numbers: str, order: List[str]) -> str:
    number_map = {number: i for (i, number) in enumerate(order)}
    numbers_list = numbers.split()
    sorted_numbers = sorted(numbers_list, key=lambda x: number_map.get(x, len(number_map)))
    return ' '.join(sorted_numbers)