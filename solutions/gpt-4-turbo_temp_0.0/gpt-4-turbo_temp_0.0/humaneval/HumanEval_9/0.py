from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:  # Check if the list is empty
        return []

    max_so_far = numbers[0]  # Initialize the first element as the maximum so far
    rolling_maxes = [max_so_far]  # Initialize the rolling maxes list with the first element

    for number in numbers[1:]:  # Iterate through the list starting from the second element
        if number > max_so_far:  # Update the maximum if the current number is greater
            max_so_far = number
        rolling_maxes.append(max_so_far)  # Append the current maximum to the rolling maxes list

    return rolling_maxes
