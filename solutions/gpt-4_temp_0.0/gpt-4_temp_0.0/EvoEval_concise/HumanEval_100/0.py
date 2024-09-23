
def make_a_pile(n):
    """
    Constructs a pile with 'n' levels of stones where the first level consists of 'n' stones. For each subsequent level,
    if 'n' is even, add the next even number of stones, if 'n' is odd, add the next odd number of stones.
    Returns a list, where each index represents the level (index+1) and its value represents the number of stones in that level.

    Example:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    pile = []
    for i in range(n):
        if n % 2 == 0:
            pile.append(n + 2 * i)
        else:
            pile.append(n + 2 * i)
    return pile