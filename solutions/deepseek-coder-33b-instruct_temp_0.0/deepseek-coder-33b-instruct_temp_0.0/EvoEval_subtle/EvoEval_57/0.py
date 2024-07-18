

def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing. If the list is empty, return False.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    >>> monotonic([])
    False
    """
    if not l:
        return False
    if len(l) < 2:
        return True
    direction = l[1] - l[0]
    for i in range(2, len(l)):
        if (l[i] - l[i - 1]) * direction < 0:
            return False
    return True