
def sorted_list_sum(lst):
    lst[:] = [s for s in lst if len(s) % 2 == 0]
    lst.sort(key=lambda s: (len(s), s))
    return lst