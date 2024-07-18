
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
    else:
        l.sort()
        n = len(l)
        m = n - 1
        return (l[n // 2] + l[m // 2]) / 2