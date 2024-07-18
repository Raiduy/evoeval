
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Return the list in the reverse order of the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [4, 3, 1]
    """
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return [number for number in reversed(numbers) if number not in duplicates]