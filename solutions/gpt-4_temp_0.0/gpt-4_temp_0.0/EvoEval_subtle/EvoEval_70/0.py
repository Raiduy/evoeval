
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
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(-1))
        if lst:
            result.append(lst.pop(0))
    return result