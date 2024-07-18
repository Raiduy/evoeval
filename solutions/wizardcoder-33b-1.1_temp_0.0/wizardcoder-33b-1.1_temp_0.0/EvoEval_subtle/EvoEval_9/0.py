
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
    """
    min_numbers = []
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
        min_numbers.append(current_min)
    return min_numbers