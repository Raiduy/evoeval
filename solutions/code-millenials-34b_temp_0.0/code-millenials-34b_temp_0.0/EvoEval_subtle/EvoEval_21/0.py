
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1. Return the list in descending order.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [1.0, 0.75, 0.5, 0.25, 0.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    scaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]
    return sorted(scaled_numbers, reverse=True)