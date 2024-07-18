

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
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
    # Create a set to store the elements of the list
    elements = set()

    # Iterate over the list
    for num in l:
        # If the negative of the current number is in the set, return True
        if -num in elements:
            return True
        # Otherwise, add the current number to the set
        elements.add(num)

    # If no two elements sum to zero, return False
    return False
