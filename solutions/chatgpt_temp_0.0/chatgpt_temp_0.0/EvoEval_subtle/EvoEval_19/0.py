
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from largest to smallest
    >>> sort_numbers('three one five')
    'five three one'
    """
    numeral_to_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numerals = numbers.split()
    numbers = [numeral_to_number[numeral] for numeral in numerals]
    numbers.sort(reverse=True)
    sorted_numerals = [numeral for number in numbers for (numeral, value) in numeral_to_number.items() if value == number]
    sorted_numbers = ' '.join(sorted_numerals)
    return sorted_numbers