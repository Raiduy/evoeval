
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    if not numbers:
        return []
    min_num = numbers[0]
    result = []
    for num in numbers:
        if num < min_num:
            min_num = num
        result.append(min_num)
    return result