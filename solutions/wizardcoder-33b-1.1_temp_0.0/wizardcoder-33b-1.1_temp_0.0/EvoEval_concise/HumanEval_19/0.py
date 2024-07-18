from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input: A string of space-separated numerals from 'zero' to 'nine'.
    Output: Returns the input string sorted in ascending order.
    >>> sort_numbers('three one five')
    'one three five'
    """
    word_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    words = numbers.split()
    sorted_numbers = sorted((word_to_num[word] for word in words))
    sorted_words = [word for (word, num) in word_to_num.items() if num in sorted_numbers]
    return ' '.join(sorted_words)