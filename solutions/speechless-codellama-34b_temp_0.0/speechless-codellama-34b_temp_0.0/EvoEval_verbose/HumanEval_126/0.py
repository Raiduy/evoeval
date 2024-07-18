def is_sorted(lst):
    if lst != sorted(lst):
        return False
    for num in lst:
        if lst.count(num) > 1:
            return False
    return True