
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1. Return the list in descending order.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [1.0, 0.75, 0.5, 0.25, 0.0]
    """
    if len(numbers) < 2:
        raise ValueError('List must contain at least two elements.')
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num
    if range_num == 0:
        return [0.0] * len(numbers)
    rescaled_numbers = [(num - min_num) / range_num for num in numbers]
    rescaled_numbers.sort(reverse=True)
    return rescaled_numbers