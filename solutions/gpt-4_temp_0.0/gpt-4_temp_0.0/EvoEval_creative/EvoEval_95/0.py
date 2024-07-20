def matrixMystery(m):
    """Write a function that takes a 2D array of integers as input (a matrix m) and returns 
    the absolute difference between the sum of the diagonals. For the purpose of this problem, 
    the diagonals are defined as follows: 

    - The first diagonal starts at the top left corner and descends down to the right (i.e., along the line of m[i][i] for all i)
    - The second diagonal starts at the top right corner and descends down to the left (i.e., along the line of m[i][len(m)-i-1] for all i)

    If the matrix is not square, return 'Invalid Matrix'.

    Example:
    matrixMystery([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) => 0
    matrixMystery([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) => 2
    matrixMystery([[1, 2], [3, 4]]) => 0
    """
    if len(m) != len(m[0]):
        return 'Invalid Matrix'
    diag1 = sum((m[i][i] for i in range(len(m))))
    diag2 = sum((m[i][len(m) - i - 1] for i in range(len(m))))
    return abs(diag1 - diag2)