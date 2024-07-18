from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Given a list of integers, this function generates and returns a new list where each element in the list
    is the maximum integer encountered in the input list until that point in the sequence.
    
    In other words, for each element in the input list, the function checks all previous numbers including 
    the current number in the sequence and finds the maximum value. This maximum value is then added to the 
    new list. The function continues this process until it has iterated over the entire input list.

    Parameters:
    numbers (List[int]): A list of integers provided as input to the function.

    Returns:
    List[int]: A list of integers where each element is the rolling maximum element found until that 
    point in the sequence.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]

    The first element in the input list is 1. As there are no previous elements, 1 is considered 
    the maximum and is added to the new list. The next element is 2. The maximum of 1 and 2 is 2, 
    so 2 is added to the new list. This process continues for all elements in the input list.
    """
    max_numbers = []
    current_max = float('-inf')
    for num in numbers:
        if num > current_max:
            current_max = num
        max_numbers.append(current_max)
    return max_numbers