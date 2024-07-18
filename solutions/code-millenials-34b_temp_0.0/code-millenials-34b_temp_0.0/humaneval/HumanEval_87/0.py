
def get_row(lst, x):
    result = []
    for i, sub_lst in enumerate(lst):
        for j, val in enumerate(sub_lst):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda a: (a[0], -a[1]))
    return result
