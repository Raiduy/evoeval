def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            if i + 2 < len(lst) and lst[i] == lst[i + 2]:
                return False
    return True