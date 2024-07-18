
def strange_sort_list(lst):
    result = []
    while lst:
        # Get and remove min value
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)

        # If list is not empty, get and remove max value
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            result.append(max_val)

    return result
