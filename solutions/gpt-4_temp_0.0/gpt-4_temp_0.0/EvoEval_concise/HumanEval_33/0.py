

def sort_third(l: list):
    """Takes a list 'l' and returns a new list with l's elements at indices divisible by three sorted, while other elements remain the same.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_elements = [l[i] for i in range(0, len(l), 3)]
    third_elements.sort()
    for (i, e) in enumerate(third_elements):
        l[i * 3] = e
    return l