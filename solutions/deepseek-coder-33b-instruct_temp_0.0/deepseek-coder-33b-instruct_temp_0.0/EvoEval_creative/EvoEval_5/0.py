from typing import List, Tuple


def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    direction = 1
    for col in range(cols):
        if direction == 1:
            for row in range(rows):
                result.append(matrix[row][col])
                col += 1
                if col == cols:
                    col -= 1
                    break
            direction = -1
        else:
            for row in range(rows - 1, -1, -1):
                result.append(matrix[row][col])
                col += 1
                if col == cols:
                    col -= 1
                    break
            direction = 1
    return result