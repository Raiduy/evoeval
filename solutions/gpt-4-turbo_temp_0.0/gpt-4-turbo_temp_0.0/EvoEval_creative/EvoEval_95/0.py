def matrixMystery(m):
    if len(m) == 0 or len(m) != len(m[0]):
        return 'Invalid Matrix'
    sum_diag1 = 0
    sum_diag2 = 0
    for i in range(len(m)):
        sum_diag1 += m[i][i]
    for i in range(len(m)):
        sum_diag2 += m[i][len(m) - i - 1]
    return abs(sum_diag1 - sum_diag2)