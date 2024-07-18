

def pairs_sum_to_zero(l):
    """
    Takes a list of integers (l) as input. Returns True if a pair of distinct elements sum to zero; otherwise, returns False.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    elements_set = set(l)
    for element in l:
        if -element in elements_set:
            if element == 0:
                if l.count(0) >= 2:
                    return True
            else:
                return True
    return False