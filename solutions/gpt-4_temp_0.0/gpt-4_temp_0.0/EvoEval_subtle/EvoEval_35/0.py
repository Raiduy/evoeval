
def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    if not l:
        return None
    min_val = l[0]
    for i in l:
        if i < min_val:
            min_val = i
    return min_val