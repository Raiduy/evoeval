from typing import List

def is_valid_input(numbers: List[float]) -> bool:
    """ Check if the input list is not empty and contains only numbers
    Args:
    numbers : List[float] - A list of float numbers
    Returns:
    bool - True if the list is not empty and contains only numbers, False otherwise
    """
    if not numbers:
        return False
    for num in numbers:
        if not isinstance(num, (int, float)):
            return False
    return True

def has_positive_values(numbers: List[float]) -> bool:
    """ Check if the input list contains at least one positive number
    Args:
    numbers : List[float] - A list of float numbers
    Returns:
    bool - True if the list contains at least one positive number, False otherwise
    """
    for num in numbers:
        if num > 0:
            return True
    return False

def calculate_geometric_mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the geometric mean.
    The geometric mean is the nth root of the product of n numbers, 
    and is used when comparing different items— like growth rates —so that 
    some numbers do not disproportionately affect the result.
    If the product of the numbers is too large for your computer's processor, 
    you should use a logarithmic method to calculate the geometric mean.
    
    Args:
    numbers : List[float] - A list of float numbers

    Returns:
    float - The Geomorphic mean of the list of numbers

    Raises:
    ValueError: If the list is empty, contains non-numeric values or does not have any positive numbers
    
    Round final answer to two decimal places
    
    >>> calculate_geometric_mean([1.0, 2.0, 3.0, 4.0])
    2.21
    """
    if not is_valid_input(numbers) or not has_positive_values(numbers):
        raise ValueError('Invalid input. List should not be empty, should contain only numbers and should have at least one positive number.')
    product = 1.0
    for num in numbers:
        product *= num
    geometric_mean = math.pow(product, 1.0 / len(numbers))
    return round(geometric_mean, 2)