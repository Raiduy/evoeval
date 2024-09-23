

def sort_even(l: list):
    """Takes a list l and returns a new list where odd-indexed elements are unchanged, while even-indexed elements are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indexed_elements = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    new_list = l.copy()
    j = 0
    for i in range(len(l)):
        if i % 2 == 0:
            new_list[i] = even_indexed_elements[j]
            j += 1
    return new_list