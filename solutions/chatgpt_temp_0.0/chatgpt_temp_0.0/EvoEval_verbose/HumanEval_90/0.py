
def next_smallest(lst):
    if len(lst) < 2 or len(set(lst)) == 1:
        return None
    sorted_lst = sorted(lst)
    return sorted_lst[1]