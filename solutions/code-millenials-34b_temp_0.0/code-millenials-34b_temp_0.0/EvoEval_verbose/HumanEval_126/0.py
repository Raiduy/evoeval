def is_sorted(lst):
    if lst != sorted(lst):
        return False
    else:
        for i in range(len(lst)):
            if lst.count(lst[i]) > 1:
                return False
        return True