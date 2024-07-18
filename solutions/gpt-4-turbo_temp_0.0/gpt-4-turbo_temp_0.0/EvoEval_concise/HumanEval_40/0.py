

def triples_sum_to_zero(l: list):
    """
    Check if there are three distinct elements in the given list of integers that sum to zero. If yes, return True, otherwise return False.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    l.sort()
    n = len(l)
    for i in range(n - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        (left, right) = (i + 1, n - 1)
        while left < right:
            total = l[i] + l[left] + l[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1
    return False