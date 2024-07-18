from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return an empty list
        return []
    
    result = [numbers[0]]  # Initialize the result list with the first element of the input list
    for number in numbers[1:]:  # Iterate over the input list starting from the second element
        result.append(delimiter)  # Append the delimiter to the result list
        result.append(number)  # Append the current number to the result list
    
    return result
