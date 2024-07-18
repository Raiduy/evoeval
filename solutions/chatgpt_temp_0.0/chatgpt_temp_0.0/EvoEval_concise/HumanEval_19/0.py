from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input: A string of space-separated numerals from 'zero' to 'nine'.
    Output: Returns the input string sorted in ascending order.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_to_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numerals = numbers.split()
    numbers = [numeral_to_number[numeral] for numeral in numerals]
    numbers.sort()
    sorted_numerals = [numeral for number in numbers for (numeral, num) in numeral_to_number.items() if num == number]
    sorted_numbers = ' '.join(sorted_numerals)
    return sorted_numbers