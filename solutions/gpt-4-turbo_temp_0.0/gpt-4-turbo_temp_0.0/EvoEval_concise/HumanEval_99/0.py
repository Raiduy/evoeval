
def closest_integer(value):
    """
    This function takes a string of a number as an input and returns the nearest 
    integer to the provided number. If the number falls midway between two integers, 
    the function rounds away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    num = float(value)
    rounded_num = int(round(num))
    return rounded_num