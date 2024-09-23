
def circular_shift(x, shift):
    """Performs a circular right shift on the digits of x as per shift value and returns the result in string format.
    Returns reversed digits if shift exceeds number of digits.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = str(x)
    shift = shift % len(x)
    return x[-shift:] + x[:-shift]