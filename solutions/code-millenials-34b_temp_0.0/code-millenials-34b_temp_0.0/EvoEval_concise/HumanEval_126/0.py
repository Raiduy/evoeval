
def is_sorted(lst):
    if len(lst) == 1:
        return True
    elif len(lst) == 2:
        return lst[0] < lst[1]
    else:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True