
def strange_sort_list(lst):
    if not lst:
        return []
    result = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            result.append(max_val)
    return result