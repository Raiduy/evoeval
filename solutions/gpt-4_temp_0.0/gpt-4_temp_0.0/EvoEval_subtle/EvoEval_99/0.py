
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
    float_value = float(value)
    if float_value >= 0:
        if float_value - int(float_value) < 0.5:
            return int(float_value)
        else:
            return int(float_value) + 1
    elif float_value - int(float_value) > -0.5:
        return int(float_value)
    else:
        return int(float_value) - 1