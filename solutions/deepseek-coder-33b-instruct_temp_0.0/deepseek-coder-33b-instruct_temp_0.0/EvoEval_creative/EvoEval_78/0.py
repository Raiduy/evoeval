def find_pattern(mat):
    n = len(mat)
    pattern = []
    for i in range(n):
        pattern.append(mat[i][i])
        pattern.append(mat[i][n - i - 1])
    return pattern