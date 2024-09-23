
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    if not numbers:
        return []
    min_list = [numbers[0]]
    for num in numbers[1:]:
        if num < min_list[-1]:
            min_list.append(num)
        else:
            min_list.append(min_list[-1])
    return min_list