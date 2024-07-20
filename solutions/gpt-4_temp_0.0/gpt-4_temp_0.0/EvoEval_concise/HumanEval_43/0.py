

def pairs_sum_to_zero(l):
    """
    Takes a list of integers (l) as input. Returns True if a pair of distinct elements sum to zero; otherwise, returns False.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    True
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    s = set()
    for num in l:
        if -num in s:
            return True
        s.add(num)
    return False