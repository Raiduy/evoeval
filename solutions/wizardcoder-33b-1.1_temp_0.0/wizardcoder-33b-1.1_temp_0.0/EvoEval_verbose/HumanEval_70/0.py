
def strange_sort_list(lst):
    sorted_lst = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        sorted_lst.append(min_val)
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            sorted_lst.append(max_val)
    return sorted_lst