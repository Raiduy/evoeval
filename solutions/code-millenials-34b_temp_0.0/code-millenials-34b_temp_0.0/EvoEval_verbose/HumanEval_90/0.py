
def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        min1 = min(lst)
        lst = [i for i in lst if i != min1]
        if len(lst) < 2:
            return None
        else:
            return min(lst)