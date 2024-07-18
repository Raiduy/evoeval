
def circular_shift(x, shift):
    """Performs a circular right shift on the digits of x as per shift value and returns the result in string format.
    Returns reversed digits if shift exceeds number of digits.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    if shift > len(str_x):
        return str_x[::-1]
    else:
        return str_x[-shift:] + str_x[:-shift]