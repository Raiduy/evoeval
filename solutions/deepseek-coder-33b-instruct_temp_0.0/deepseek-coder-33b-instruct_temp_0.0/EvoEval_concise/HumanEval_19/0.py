from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input: A string of space-separated numerals from 'zero' to 'nine'.
    Output: Returns the input string sorted in ascending order.
    >>> sort_numbers('three one five')
    'one three five'
    """
    order = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_list = numbers.split()
    sorted_list = sorted(numbers_list, key=order.index)
    sorted_string = ' '.join(sorted_list)
    return sorted_string