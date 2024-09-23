
from typing import List

def max_close_element_difference(numbers: List[float], threshold: float) -> float:
    """
    Given a list of numbers and a threshold, find two elements that are closer to each other than the threshold and return their difference. If multiple pairs meet the criteria, return the maximum difference. If no such pairs exist, return 0.
    >>> max_close_element_difference([1.0, 2.0, 3.0], 0.5)
    0
    >>> max_close_element_difference([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    0.2
    >>> max_close_element_difference([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 5)
    4
    """
    max_diff = 0
    numbers.sort()
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < threshold:
            max_diff = max(max_diff, diff)
    return max_diff