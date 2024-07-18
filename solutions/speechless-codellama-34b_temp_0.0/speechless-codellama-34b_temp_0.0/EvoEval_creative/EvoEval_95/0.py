def matrixMystery(m):
    if len(m) != len(m[0]):
        return 'Invalid Matrix'
    diagonal1_sum = 0
    diagonal2_sum = 0
    for i in range(len(m)):
        diagonal1_sum += m[i][i]
        diagonal2_sum += m[i][len(m) - i - 1]
    return abs(diagonal1_sum - diagonal2_sum)