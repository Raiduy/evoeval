from typing import List, Tuple


def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
    result = []
    row = 0
    col = 0
    direction = (1, 1)
    while len(result) < len(matrix) * len(matrix[0]):
        result.append(matrix[row][col])
        if direction == (1, 1) and (col == len(matrix[0]) - 1 or row == len(matrix) - 1):
            if col == len(matrix[0]) - 1:
                row += 1
            else:
                col += 1
            direction = (-1, -1)
        elif direction == (-1, -1) and (col == 0 or row == 0):
            if col == 0:
                row -= 1
            else:
                col -= 1
            direction = (1, 1)
        else:
            row += direction[0]
            col += direction[1]
    return result