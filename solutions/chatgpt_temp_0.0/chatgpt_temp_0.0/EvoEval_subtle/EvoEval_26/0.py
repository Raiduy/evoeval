
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Return the list in the reverse order of the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [4, 3, 1]
    """
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    unique_numbers = []
    for num in reversed(numbers):
        if count_dict[num] == 1:
            unique_numbers.append(num)
    return unique_numbers