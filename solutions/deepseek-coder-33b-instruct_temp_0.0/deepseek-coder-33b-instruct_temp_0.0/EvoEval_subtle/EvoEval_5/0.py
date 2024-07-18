
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers' and add 'delimeter' at the end of the list
    >>> intersperse([], 4)
    [4]
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3, 4]
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    result.append(delimeter)
    return result