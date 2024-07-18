
def circular_shift(x, shift):
    """Performs a circular right shift on the digits of x as per shift value and returns the result in string format.
    Returns reversed digits if shift exceeds number of digits.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    n = len(x_str)
    if shift >= n:
        return x_str[::-1]
    shift = shift % n
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str