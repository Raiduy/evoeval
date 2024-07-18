
def circular_shift(x, shift):
    """Performs a circular right shift on the digits of x as per shift value and returns the result in string format.
    Returns reversed digits if shift exceeds number of digits.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    shifted_str_x = str_x[-shift:] + str_x[:-shift]
    return shifted_str_x