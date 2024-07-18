from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    # sort the numbers
    numbers.sort()

    # initialize variables
    min_diff = float('inf')
    result = None

    # loop through the numbers
    for i in range(1, len(numbers)):
        # calculate the difference
        diff = numbers[i] - numbers[i-1]
        # if the difference is smaller than min_diff, update min_diff and result
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i-1], numbers[i])

    return result
