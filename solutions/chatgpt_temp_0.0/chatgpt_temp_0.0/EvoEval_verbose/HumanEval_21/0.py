from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of floating point numbers, this function applies a linear transformation to each element in the list
    in such a way that the smallest number in the initial list becomes 0 and the largest number becomes 1 in the resulting list. 

    The function assumes that the input list contains at least two elements.

    Each element in the transformed list corresponds to the rescaled value of the corresponding element in the original list.
    
    This operation is useful in machine learning and data analysis, where it is often required to normalize or standardize data. 

    Args:
    numbers (List[float]): A list of floating point numbers. It is assumed that the list contains at least two distinct numbers.

    Returns:
    List[float]: A list containing the rescaled numbers. The smallest number in the original list is transformed to 0,
    and the largest number is transformed to 1. All other numbers are linearly transformed to a number between 0 and 1.

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    scaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]
    return scaled_numbers