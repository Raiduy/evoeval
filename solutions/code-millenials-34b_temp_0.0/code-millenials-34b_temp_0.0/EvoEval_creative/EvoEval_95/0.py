def matrixMystery(m):
    if len(m) != len(m[0]):
        return 'Invalid Matrix'
    first_diagonal_sum = sum((m[i][i] for i in range(len(m))))
    second_diagonal_sum = sum((m[i][len(m) - i - 1] for i in range(len(m))))
    return abs(first_diagonal_sum - second_diagonal_sum)