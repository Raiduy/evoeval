

def least_common_multiple(a: int, b: int) -> int:
    """ Return the least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """
    max_num = max(a, b)
    lcm = max_num
    while lcm % a != 0 or lcm % b != 0:
        lcm += max_num
    return lcm