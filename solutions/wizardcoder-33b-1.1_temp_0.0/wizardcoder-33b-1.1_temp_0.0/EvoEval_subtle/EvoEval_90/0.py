
def next_largest(lst):
    if len(lst) < 2:
        return None
    else:
        lst = list(set(lst))
        lst.sort()
        return lst[-2]