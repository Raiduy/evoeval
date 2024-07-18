

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted in descending order.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [5, 6, 3, 4]
    """
    even_indices = [l[i] for i in range(0, len(l), 2)]
    even_indices.sort(reverse=True)
    for (i, val) in enumerate(even_indices):
        l[2 * i] = val
    return l