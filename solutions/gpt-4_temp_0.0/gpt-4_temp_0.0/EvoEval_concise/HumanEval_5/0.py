from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert 'delimeter' between each pair of elements in `numbers'.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.extend([num, delimeter])
    return result[:-1]