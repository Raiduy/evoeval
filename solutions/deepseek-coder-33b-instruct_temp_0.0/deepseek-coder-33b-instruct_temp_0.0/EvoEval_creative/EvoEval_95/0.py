def matrixMystery(m):
    if len(m) != len(m[0]):
        return 'Invalid Matrix'
    sum1 = 0
    sum2 = 0
    for i in range(len(m)):
        sum1 += m[i][i]
        sum2 += m[i][len(m) - i - 1]
    return abs(sum1 - sum2)