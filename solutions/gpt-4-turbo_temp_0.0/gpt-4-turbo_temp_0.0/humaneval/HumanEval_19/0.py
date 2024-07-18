from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping of number words to their numeric values
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # Split the input string into a list of number words
    number_words = numbers.split()
    
    # Sort the list of number words based on their numeric value
    sorted_number_words = sorted(number_words, key=lambda word: number_map[word])
    
    # Join the sorted list back into a string and return it
    return ' '.join(sorted_number_words)
