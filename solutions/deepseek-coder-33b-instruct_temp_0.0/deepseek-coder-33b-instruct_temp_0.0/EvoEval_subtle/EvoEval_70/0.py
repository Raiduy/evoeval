
def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the maximum value,
    then minimum of the remaining integers, then maximum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [4, 1, 3, 2]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    result = []
    while lst:
        max_value = max(lst)
        lst.remove(max_value)
        result.append(max_value)
        if lst:
            min_value = min(lst)
            lst.remove(min_value)
            result.append(min_value)
    return result