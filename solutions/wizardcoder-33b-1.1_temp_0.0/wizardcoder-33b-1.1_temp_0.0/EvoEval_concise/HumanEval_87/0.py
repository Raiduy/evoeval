
def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 1, -1, -1):
            if lst[i][j] == x:
                result.append((i, j))
    return result