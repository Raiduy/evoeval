
def triples_sum_to_ten(l: list):
    """
    triples_sum_to_ten takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to ten, and False otherwise.

    >>> triples_sum_to_ten([1, 3, 5, 0])
    False
    >>> triples_sum_to_ten([1, 3, -2, 1])
    False
    >>> triples_sum_to_ten([1, 2, 3, 7])
    True
    >>> triples_sum_to_ten([2, 4, -5, 3, 9, 7])
    False
    >>> triples_sum_to_ten([1])
    False
    """
    if len(l) < 3:
        return False
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 10:
                    return True
    return False