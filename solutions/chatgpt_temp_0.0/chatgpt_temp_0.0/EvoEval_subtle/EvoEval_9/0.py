
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    rolling_min_list = []
    current_min = float('inf')
    for num in numbers:
        current_min = min(current_min, num)
        rolling_min_list.append(current_min)
    return rolling_min_list