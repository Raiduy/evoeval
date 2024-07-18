from typing import List


def sort_numbers(numbers: str) -> str:
    name_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_to_name = {value: key for (key, value) in name_to_num.items()}
    number_names = numbers.split()
    number_values = [name_to_num[name] for name in number_names]
    number_values.sort()
    sorted_names = [num_to_name[value] for value in number_values]
    return ' '.join(sorted_names)