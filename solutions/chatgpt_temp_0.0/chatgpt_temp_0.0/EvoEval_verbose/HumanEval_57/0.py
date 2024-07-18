

def monotonic(l: list) -> bool:
    """
    This function takes in a list of integers or floats as its input and checks whether the elements in the list are 
    monotonically increasing or decreasing. 

    Monotonically increasing means that each subsequent element in the list is greater than or equal to the previous one, 
    while monotonically decreasing means that each subsequent element in the list is less than or equal to the previous one. 

    If the list is either monotonically increasing or decreasing, the function will return a boolean value of True. 
    If the list is not monotonically increasing or decreasing, the function will return a boolean value of False.

    Args:
    l (list): A list of numbers (integers or floats)

    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    This example returns True because the list is monotonically increasing.

    >>> monotonic([1, 20, 4, 10])
    False
    This example returns False because the list is not monotonically increasing nor decreasing.

    >>> monotonic([4, 1, 0, -10])
    True
    This example returns True because the list is monotonically decreasing.
    """
    if len(l) <= 1:
        return True
    increasing = all((l[i] <= l[i + 1] for i in range(len(l) - 1)))
    decreasing = all((l[i] >= l[i + 1] for i in range(len(l) - 1)))
    return increasing or decreasing