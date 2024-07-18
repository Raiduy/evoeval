from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    This function takes as input a list of numbers (floats), of length at least two, and finds the pair of numbers that are the closest to each other. 
    The function returns this pair of numbers in order, with the smaller number first and the larger number second. 
    
    If there are multiple pairs with the same smallest difference, the function will return the first pair it encounters.

    The main purpose of this function is to aid in numerical analysis, where finding the smallest difference between pairs of numbers can be useful for things like error detection, curve fitting, and other analysis tasks.

    Args:
    numbers (List[float]): A list of floating point numbers. The list should contain at least two elements. 

    Returns:
    Tuple[float, float]: A tuple containing two floating point numbers that have the smallest difference among all possible pairs in the input list. The smaller number is returned first.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    min_diff = float('inf')
    closest_pair = None
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair