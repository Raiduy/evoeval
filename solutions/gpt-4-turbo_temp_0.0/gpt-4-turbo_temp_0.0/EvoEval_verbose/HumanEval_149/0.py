
def sorted_list_sum(lst):
    lst = [s for s in lst if len(s) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst