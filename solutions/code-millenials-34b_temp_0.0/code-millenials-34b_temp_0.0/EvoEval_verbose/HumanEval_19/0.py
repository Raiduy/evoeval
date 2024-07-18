from typing import List


def sort_numbers(numbers: str) -> str:
    number_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numeric_values = [number_map[number] for number in numbers.split()]
    numeric_values.sort()
    sorted_names = [key for (key, value) in number_map.items() if value in numeric_values]
    return ' '.join(sorted_names)