

def sort_even(l: list):
    """Takes a list l and returns a new list where odd-indexed elements are unchanged, while even-indexed elements are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indexed = sorted(l[::2])
    sorted_list = []
    for (i, num) in enumerate(l):
        if i % 2 == 0:
            sorted_list.append(even_indexed.pop(0))
        else:
            sorted_list.append(num)
    return sorted_list