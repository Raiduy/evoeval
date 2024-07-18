
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Return the list in the reverse order of the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [4, 3, 1]
    """
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    unique_numbers = []
    for num in reversed(numbers):
        if freq[num] == 1:
            unique_numbers.append(num)
            del freq[num]
    return unique_numbers