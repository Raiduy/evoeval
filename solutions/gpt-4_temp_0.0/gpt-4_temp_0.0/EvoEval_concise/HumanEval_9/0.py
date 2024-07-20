from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ Generates a list with the maximum element found till that index in the given list of integers.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
        max_list.append(current_max)
    return max_list