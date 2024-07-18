def is_sorted(lst):
    if lst != sorted(lst):
        return False
    if len(lst) != len(set(lst)):
        return False
    return True