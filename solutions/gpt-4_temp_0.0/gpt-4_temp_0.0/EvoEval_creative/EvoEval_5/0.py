from typing import List, Tuple


def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
    """Given a 2D list of integers, return a list that represents its elements traversed in a zigzag order starting from the top-left corner and moving rightwards.
    When the right end is reached, the direction should be downwards to the next row, then to the left end, and so on until all elements are covered. 
    >>> zigzag_traversal([[1, 2], [3, 4], [5, 6, 7], [8, 9, 10]])
    [1, 2, 4, 3, 5, 6, 7, 10, 9, 8]
    """
    result = []
    flip = False
    for row in matrix:
        if flip:
            result.extend(row[::-1])
        else:
            result.extend(row)
        flip = not flip
    return result