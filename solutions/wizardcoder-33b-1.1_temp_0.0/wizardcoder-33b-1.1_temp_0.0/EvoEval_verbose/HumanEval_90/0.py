
def next_smallest(lst):
    if len(lst) == 0 or len(set(lst)) == 1:
        return None
    else:
        lst.sort()
        return lst[1]