def get_row(lst, x, y):
    result = []
    for (i, row) in enumerate(lst):
        for (j, col) in enumerate(row):
            for (k, depth) in enumerate(col):
                if depth == x:
                    if y != depth:
                        result.append((i, j, k))
    result.sort(key=lambda a: (a[0], -a[1], a[2]))
    return result