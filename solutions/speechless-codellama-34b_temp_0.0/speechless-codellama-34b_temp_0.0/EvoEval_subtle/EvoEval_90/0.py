
def next_largest(lst):
    if len(lst) < 2:
        return None
    max_val = max(lst)
    lst.remove(max_val)
    max_val_2 = max(lst)
    return max_val_2