
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists in descending order.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [653, 5, 1]
    >>> common([5, 3, 2, 8], [3, 2])
    [3, 2]

    """
    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1 & set2
    common_elements_list = list(common_elements)
    common_elements_list.sort(reverse=True)
    return common_elements_list