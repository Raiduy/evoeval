from typing import List


def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])
    sorted_numbers = ' '.join(sorted_num_list)
    return sorted_numbers