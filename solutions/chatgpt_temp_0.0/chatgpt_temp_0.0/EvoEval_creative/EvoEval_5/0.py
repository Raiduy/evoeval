from typing import List, Tuple


def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
    """Given a 2D list of integers, return a list that represents its elements traversed in a zigzag order starting from the top-left corner and moving rightwards.
    When the right end is reached, the direction should be downwards to the next row, then to the left end, and so on until all elements are covered. 
    >>> zigzag_traversal([[1, 2], [3, 4], [5, 6, 7], [8, 9, 10]])
    [1, 2, 4, 3, 5, 6, 7, 10, 9, 8]
    """
    if not matrix:
        return []
    rows = len(matrix)
    cols = max((len(row) for row in matrix))
    result = []
    direction = 1
    (row, col) = (0, 0)
    while row < rows and col < cols:
        result.append(matrix[row][col])
        if direction == 1:
            if col == cols - 1:
                row += 1
                direction = -1
            elif row == 0:
                col += 1
                direction = -1
            else:
                row -= 1
                col += 1
        elif row == rows - 1:
            col += 1
            direction = 1
        elif col == 0:
            row += 1
            direction = 1
        else:
            row += 1
            col -= 1
    return result