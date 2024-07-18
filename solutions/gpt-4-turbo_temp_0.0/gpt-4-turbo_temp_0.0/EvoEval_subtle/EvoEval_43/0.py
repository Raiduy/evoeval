
def pairs_sum_to_one(l):
    """
    pairs_sum_to_one takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to one, and False otherwise.
    >>> pairs_sum_to_one([1, 3, 5, 0])
    True
    >>> pairs_sum_to_one([1, 3, -2, 1])
    True
    >>> pairs_sum_to_one([1, 2, 3, 7])
    False
    >>> pairs_sum_to_one([2, 4, -5, 3, 5, 7])
    False
    >>> pairs_sum_to_one([1])
    False
    """
    elements = set(l)
    for item in elements:
        if 1 - item in elements and 1 - item != item:
            return True
    return False