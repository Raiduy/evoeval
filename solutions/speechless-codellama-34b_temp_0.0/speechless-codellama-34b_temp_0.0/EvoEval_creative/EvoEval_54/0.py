def find_star_map(lst, star):
    result = []
    for (i, row) in enumerate(lst):
        for (j, col) in enumerate(row):
            if col == star:
                result.append((i, j))
    return result