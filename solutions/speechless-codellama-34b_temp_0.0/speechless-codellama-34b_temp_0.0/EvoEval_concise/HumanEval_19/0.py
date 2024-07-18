from typing import List


def sort_numbers(numbers: str) -> str:
    numerals = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sorted_numbers = sorted(numbers.split(), key=lambda x: numerals[x])
    return ' '.join(sorted_numbers)