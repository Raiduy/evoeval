
def special_stone_factorial(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones. The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.

    For each level, calculate the Brazilian factorial (defined as: brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!), 
    where n is the number of stones in the level.

    Return the list of Brazilian factorials for each level.

    For example:
    >>> special_stone_factorial(3)
    [12, 34560, 125411328000]
    """
    result = []
    for i in range(n, 0, -1):
        result.append(brazilian_factorial(i))
    return result