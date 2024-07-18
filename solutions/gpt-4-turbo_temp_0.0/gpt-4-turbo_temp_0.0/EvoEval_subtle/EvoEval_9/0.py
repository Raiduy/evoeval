
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    if not numbers:
        return []
    rolling_mins = [numbers[0]]
    for number in numbers[1:]:
        rolling_mins.append(min(number, rolling_mins[-1]))
    return rolling_mins