
def median(l: list):
    """Return median of elements in the list l, but if the list is empty, return 0 instead.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    >>> median([])
    0
    """
    if not l:
        return 0
    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2