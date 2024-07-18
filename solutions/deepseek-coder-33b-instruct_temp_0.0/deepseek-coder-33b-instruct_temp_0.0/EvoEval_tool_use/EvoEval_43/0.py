from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """Transpose a given matrix.

    Args:
        matrix: A 2D list of integers representing the matrix to transpose.

    Returns:
        A new 2D list of integers representing the transposed matrix.
    """
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed
from typing import List

def rotate_matrix_90_degrees_clockwise(matrix: List[List[int]]) -> List[List[int]]:
    """Rotate a given square matrix 90 degrees clockwise.

    Args:
        matrix: A 2D list of integers representing the matrix to rotate.

    Returns:
        A new 2D list of integers representing the rotated matrix.

    Note: 
        This function assumes that the input matrix is a square matrix (i.e., number of rows equals number of columns).

    Examples:
        >>> rotate_matrix_90_degrees_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        >>> rotate_matrix_90_degrees_clockwise([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
    """
    n = len(matrix)
    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][n - 1 - i] = matrix[i][j]
    return transposed