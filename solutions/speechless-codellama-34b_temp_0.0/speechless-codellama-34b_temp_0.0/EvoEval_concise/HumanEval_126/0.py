
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        if lst[i] == lst[i + 1] and (i > 0 and lst[i - 1] != lst[i]):
            return False
    return True