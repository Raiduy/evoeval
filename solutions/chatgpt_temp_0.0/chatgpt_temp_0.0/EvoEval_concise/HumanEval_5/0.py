from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert 'delimiter' between each pair of elements in `numbers'.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(len(numbers)):
        if i != 0:
            result.append(delimiter)
        result.append(numbers[i])
    return result