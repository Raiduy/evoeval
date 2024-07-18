
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # Initialize the list with the first level
    stones = [n]
    # Loop to fill up the rest of the levels
    for i in range(1, n):
        # Check if the last number of stones added was odd or even
        if stones[-1] % 2 == 0:  # If even
            stones.append(stones[-1] + 2)  # Add the next even number
        else:  # If odd
            stones.append(stones[-1] + 2)  # Add the next odd number
    return stones
