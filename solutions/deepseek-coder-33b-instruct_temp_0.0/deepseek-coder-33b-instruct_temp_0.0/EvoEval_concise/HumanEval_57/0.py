

def monotonic(l: list):
    """Checks if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            increasing = False
        if l[i] < l[i + 1]:
            decreasing = False
    return increasing or decreasing