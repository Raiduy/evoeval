
def strange_sort_list(lst):
    """
    Sorts a list of integers in a specific order: start with the smallest value, 
    then the largest of the remaining, then smallest, and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())
    return result