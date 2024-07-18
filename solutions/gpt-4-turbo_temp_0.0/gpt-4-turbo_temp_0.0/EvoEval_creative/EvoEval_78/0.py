def find_pattern(mat):
    n = len(mat)
    pattern = []
    for i in range(n):
        pattern.append(mat[i][i])
    for i in range(n):
        if i != n // 2:
            pattern.append(mat[i][n - 1 - i])
    return pattern