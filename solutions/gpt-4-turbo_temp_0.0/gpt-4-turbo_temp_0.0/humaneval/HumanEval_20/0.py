from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to store the closest pair found and the smallest difference found
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    smallest_difference = abs(sorted_numbers[1] - sorted_numbers[0])
    
    # Iterate through the sorted list to find the closest pair
    for i in range(1, len(sorted_numbers) - 1):
        current_difference = abs(sorted_numbers[i+1] - sorted_numbers[i])
        if current_difference < smallest_difference:
            smallest_difference = current_difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    
    return closest_pair
