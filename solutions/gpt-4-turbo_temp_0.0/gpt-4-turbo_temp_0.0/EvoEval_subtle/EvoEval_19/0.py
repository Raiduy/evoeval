
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from largest to smallest
    >>> sort_numbers('three one five')
    'five three one'
    """
    number_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    number_words = numbers.split()
    sorted_number_words = sorted(number_words, key=lambda word: number_map[word], reverse=True)
    return ' '.join(sorted_number_words)