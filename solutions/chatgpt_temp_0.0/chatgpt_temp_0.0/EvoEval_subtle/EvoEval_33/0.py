
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted in descending order.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [5, 6, 3, 4, 8, 9, 2]
    """
    sorted_values = sorted(l[::3], reverse=True)
    result = []
    for (i, value) in enumerate(l):
        if i % 3 == 0:
            result.append(sorted_values.pop(0))
        else:
            result.append(value)
    return result