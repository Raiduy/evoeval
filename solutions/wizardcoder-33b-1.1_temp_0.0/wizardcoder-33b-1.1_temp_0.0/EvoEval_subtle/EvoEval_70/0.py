
def strange_sort_list(lst):
    result = []
    while lst:
        max_val = max(lst)
        lst.remove(max_val)
        result.append(max_val)
        if lst:
            min_val = min(lst)
            lst.remove(min_val)
            result.append(min_val)
    return result