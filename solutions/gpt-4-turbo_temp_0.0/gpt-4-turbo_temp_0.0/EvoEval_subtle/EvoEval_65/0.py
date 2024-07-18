
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits left by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(21, 1)
    "12"
    >>> circular_shift(21, 2)
    "21"
    """
    x_str = str(x)
    n = len(x_str)
    if shift >= n:
        return x_str[::-1]
    shifted_str = x_str[shift:] + x_str[:shift]
    return shifted_str