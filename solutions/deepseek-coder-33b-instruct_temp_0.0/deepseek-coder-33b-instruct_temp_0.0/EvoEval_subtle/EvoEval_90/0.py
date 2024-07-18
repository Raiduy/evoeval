
def next_largest(lst):
    if len(lst) < 2:
        return None
    else:
        lst.sort()
        return lst[-2]