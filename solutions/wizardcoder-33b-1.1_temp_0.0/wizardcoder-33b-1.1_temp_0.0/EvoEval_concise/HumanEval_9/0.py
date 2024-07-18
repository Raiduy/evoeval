from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ Generates a list with the maximum element found till that index in the given list of integers.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = []
    for i in range(len(numbers)):
        if i == 0:
            max_numbers.append(numbers[i])
        else:
            max_numbers.append(max(max_numbers[i - 1], numbers[i]))
    return max_numbers