from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two adjacent numbers that are the closest to each
    other and return them in reverse order (larger number, smaller number).
    """
    closest_pair = (numbers[1], numbers[0])
    smallest_diff = abs(numbers[1] - numbers[0])
    for i in range(1, len(numbers) - 1):
        current_diff = abs(numbers[i + 1] - numbers[i])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_pair = (numbers[i + 1], numbers[i])
    return tuple(sorted(closest_pair, reverse=True))