
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Return the list in the reverse order of the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [4, 3, 1]
    """
    result = []
    for number in reversed(numbers):
        if number not in result:
            result.append(number)
    return result