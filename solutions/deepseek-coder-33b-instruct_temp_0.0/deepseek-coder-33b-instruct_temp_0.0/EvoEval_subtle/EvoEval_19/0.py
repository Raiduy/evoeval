
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from largest to smallest
    >>> sort_numbers('three one five')
    'five three one'
    """
    word_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    words = numbers.split()
    sorted_numbers = sorted(map(word_to_num.get, words), reverse=True)
    sorted_words = list(map(lambda num: next((key for (key, value) in word_to_num.items() if value == num)), sorted_numbers))
    sorted_string = ' '.join(sorted_words)
    return sorted_string