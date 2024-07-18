from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ Returns the pair of numbers from the input list that are nearest to each other, sorted in ascending order.
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    smallest_diff = abs(sorted_numbers[1] - sorted_numbers[0])
    for i in range(1, len(sorted_numbers) - 1):
        current_diff = abs(sorted_numbers[i + 1] - sorted_numbers[i])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair