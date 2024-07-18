from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input: A string of space-separated numerals from 'zero' to 'nine'.
    Output: Returns the input string sorted in ascending order.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_to_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numeral_words = numbers.split()
    numeric_values = [numeral_to_number[word] for word in numeral_words]
    sorted_numeric_values = sorted(numeric_values)
    sorted_numeral_words = [list(numeral_to_number.keys())[list(numeral_to_number.values()).index(value)] for value in sorted_numeric_values]
    sorted_numbers_str = ' '.join(sorted_numeral_words)
    return sorted_numbers_str