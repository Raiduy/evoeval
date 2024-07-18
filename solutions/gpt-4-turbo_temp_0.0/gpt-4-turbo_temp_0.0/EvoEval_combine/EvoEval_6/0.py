
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
    stones = []
    current_stones = n
    for _ in range(n):
        stones.append(current_stones)
        if current_stones % 2 == 0:
            current_stones += 2
        else:
            current_stones += 2
    stones.sort()
    mid = len(stones) // 2
    if len(stones) % 2 == 0:
        return (stones[mid - 1] + stones[mid]) / 2.0
    else:
        return stones[mid]