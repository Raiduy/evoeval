def get_row(lst, x, y):
    result = []
    for (i, row) in enumerate(lst):
        for (j, column) in enumerate(row):
            for (k, depth) in enumerate(column):
                if depth == x and k != y:
                    result.append((i, j, k))
    result.sort(key=lambda x: (x[0], -x[1], x[2]))
    return result