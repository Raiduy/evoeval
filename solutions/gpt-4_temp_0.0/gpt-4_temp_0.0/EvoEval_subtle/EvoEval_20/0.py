from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two adjacent numbers that are the closest to each
    other and return them in reverse order (larger number, smaller number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 1.0)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.5])
    (5.0, 4.5)
    """
    if len(numbers) < 2:
        raise ValueError('The list should contain at least two numbers.')
    numbers.sort()
    min_diff = float('inf')
    closest_pair = None
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i + 1], numbers[i])
    return closest_pair