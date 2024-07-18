

def sort_even(l: list):
    """Takes a list l and returns a new list where odd-indexed elements are unchanged, while even-indexed elements are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_elements = sorted(l[::2])
    for i in range(0, len(l), 2):
        l[i] = even_elements.pop(0)
    return l