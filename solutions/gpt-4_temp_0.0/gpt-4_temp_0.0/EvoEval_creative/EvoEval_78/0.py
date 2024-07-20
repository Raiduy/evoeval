def find_pattern(mat):
    n = len(mat)
    result = []
    for i in range(n):
        result.append(mat[i][i])
        result.append(mat[i][n - i - 1])
    return result