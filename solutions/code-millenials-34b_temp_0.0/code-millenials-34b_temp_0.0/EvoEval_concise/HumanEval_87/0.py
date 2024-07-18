
def get_row(lst, x):
    result = []
    for (i, sublist) in enumerate(lst):
        for j in range(len(sublist) - 1, -1, -1):
            if sublist[j] == x:
                result.append((i, j))
    return result