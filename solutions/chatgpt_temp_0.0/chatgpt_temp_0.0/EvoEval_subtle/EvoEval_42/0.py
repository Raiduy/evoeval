

def incr_list(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list([1, 2, 3])
    [3, 4, 5]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [num + 2 for num in l]