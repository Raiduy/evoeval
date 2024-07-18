
def common_pairs_with_zero_sum(l1: list, l2: list) -> bool:
    """
    common_pairs_with_zero_sum takes two lists of integers as an input.
    It first identifies the common elements between the two lists.
    Then, it checks if there are two distinct elements in the common elements that sum to zero.
    
    Returns True if such pair exists and False otherwise.

    >>> common_pairs_with_zero_sum([1, 3, 5, -3, 0], [0, -3, 1, 5, 2])
    False
    >>> common_pairs_with_zero_sum([1, 3, -2, 1], [2, 3, -2, 1])
    False
    >>> common_pairs_with_zero_sum([1, 2, 3, 7], [8, 9, 2, 1])
    False
    >>> common_pairs_with_zero_sum([2, 4, -5, 3, 5, 7], [-5, 4, 2, 3, 5, 7])
    True
    >>> common_pairs_with_zero_sum([1], [2])
    False
    """
    common_elements = set(l1) & set(l2)
    for num1 in common_elements:
        for num2 in common_elements:
            if num1 != num2 and num1 + num2 == 0:
                return True
    return False