from typing import List, Tuple


def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
    result = []
    for (direction, row) in enumerate(matrix):
        if direction % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result