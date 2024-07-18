

def sort_even(l: list):
    """Takes a list l and returns a new list where odd-indexed elements are unchanged, while even-indexed elements are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indexed_elements = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indexed_elements_sorted = sorted(even_indexed_elements)
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indexed_elements_sorted.pop(0))
        else:
            result.append(l[i])
    return result