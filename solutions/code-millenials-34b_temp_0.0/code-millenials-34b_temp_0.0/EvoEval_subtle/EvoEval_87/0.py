def get_row(lst, x):
    result = []
    for (i, sub_list) in enumerate(lst):
        for (j, val) in enumerate(sub_list):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda a: (a[0], a[1]), reverse=True)
    return result