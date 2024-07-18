from typing import List, Tuple


def sort_numbers(numbers: str, order: List[str]) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    num_list.sort(key=lambda x: (order.index(x) if x in order else len(order), num_dict[x]))
    return ' '.join(num_list)