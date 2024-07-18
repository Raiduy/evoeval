
def closest_integer(value):
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it towards zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding towards zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    closest to zero. For example closest_integer("14.5") should
    return 14 and closest_integer("-14.5") should return -14.
    """
    value = float(value)
    if value >= 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)