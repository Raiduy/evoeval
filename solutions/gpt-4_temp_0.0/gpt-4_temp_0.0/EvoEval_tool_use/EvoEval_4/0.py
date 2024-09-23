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
    if not is_valid_input(numbers):
        raise ValueError('The list is either empty or contains non-numeric values')
    if not has_positive_values(numbers):
        raise ValueError('The list does not have any positive numbers')
    log_sum = sum((math.log(n) for n in numbers))
    mean = math.exp(log_sum / len(numbers))
    return round(mean, 2)