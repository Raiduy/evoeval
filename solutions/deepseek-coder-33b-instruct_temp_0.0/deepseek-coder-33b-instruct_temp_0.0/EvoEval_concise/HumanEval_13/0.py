

def greatest_common_divisor(a: int, b: int) -> int:
    """ Returns the highest common divisor of integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a