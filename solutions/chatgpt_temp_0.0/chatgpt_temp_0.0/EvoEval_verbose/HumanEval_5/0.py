from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    This function performs an operation on a list of integers, 'numbers', and an integer, 'delimiter'.
    The operation consists of inserting the 'delimiter' between every two consecutive elements in the 'numbers' list.
    
    In other words, the function traverses the list and for each pair of consecutive numbers, it inserts the 'delimiter' in between them, thus returning a new list with the 'delimiter' interspersed between the original numbers.
    
    If the 'numbers' list is empty, the function simply returns an empty list. The 'delimiter' can be any integer.
    
    Parameters:
    numbers (List[int]): The original list of integers
    delimiter (int): The integer to be inserted between each pair of consecutive numbers in the 'numbers' list
    
    Returns:
    List[int]: A new list with the 'delimiter' inserted between each pair of consecutive numbers from the 'numbers' list
    
    
    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result