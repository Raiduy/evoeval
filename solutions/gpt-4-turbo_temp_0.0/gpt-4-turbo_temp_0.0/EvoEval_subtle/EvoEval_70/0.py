
def strange_sort_list(lst):
    result = []
    pick_max = True
    while lst:
        if pick_max:
            value = max(lst)
        else:
            value = min(lst)
        result.append(value)
        lst.remove(value)
        pick_max = not pick_max
    return result