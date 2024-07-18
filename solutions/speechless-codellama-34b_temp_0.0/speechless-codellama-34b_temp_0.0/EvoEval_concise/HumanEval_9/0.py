from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ Generates a list with the maximum element found till that index in the given list of integers.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        max_list.append(max_num)
    return max_list