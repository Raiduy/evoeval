from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input: A string of space-separated numerals from 'zero' to 'nine'.
    Output: Returns the input string sorted in ascending order.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numeral_list = numbers.split()
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_dict[x])
    return ' '.join(sorted_numerals)