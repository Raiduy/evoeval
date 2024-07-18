from typing import List, Tuple


def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
    result = []
    direction = [(-1, 1), (1, -1)]
    (row, col) = (0, 0)
    d = 0
    while len(result) < sum((len(row) for row in matrix)):
        result.append(matrix[row][col])
        (next_row, next_col) = (row + direction[d][0], col + direction[d][1])
        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[next_row]):
            (row, col) = (next_row, next_col)
        else:
            if d == 0:
                if col == len(matrix[row]) - 1:
                    row += 1
                else:
                    col += 1
            elif row == len(matrix) - 1:
                col += 1
            else:
                row += 1
            d = 1 - d
    return result