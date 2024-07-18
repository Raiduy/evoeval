from typing import List


def sort_numbers(numbers: str) -> str:
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    number_names = numbers.split()
    digits = [number_dict[name] for name in number_names]
    digits.sort()
    sorted_number_names = [name for (name, digit) in number_dict.items() if digit in digits]
    return ' '.join(sorted_number_names)