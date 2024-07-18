

def monotonic(l: list):
    """Checks if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    is_increasing = l[1] > l[0]
    for i in range(1, len(l)):
        if is_increasing and l[i] < l[i - 1]:
            return False
        elif not is_increasing and l[i] > l[i - 1]:
            return False
    return True