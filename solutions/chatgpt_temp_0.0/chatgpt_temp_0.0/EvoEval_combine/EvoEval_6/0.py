
def pile_median(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the median number of stones in all levels in the pile.

    You should return the answer as a float if the number of levels is even,
    and as an integer if the number of levels is odd.

    Examples:
    >>> pile_median(3)
    5
    >>> pile_median(4)
    7.0
    """
    if n % 2 == 0:
        return float(n + (n - 1)) / 2
    else:
        return (n + (n - 1)) // 2 + 1