
def get_row(lst, x):
    result = []
    for (i, row) in enumerate(lst):
        for (j, val) in enumerate(row):
            if val == x:
                result.append((i, j))
    return result