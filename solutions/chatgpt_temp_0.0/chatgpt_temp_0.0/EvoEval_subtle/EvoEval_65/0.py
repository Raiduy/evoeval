
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits left by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x_str = str(x)
    num_digits = len(x_str)
    shift %= num_digits
    if shift == 0:
        return x_str
    shifted_str = x_str[shift:] + x_str[:shift]
    if shift > num_digits // 2:
        shifted_str = shifted_str[::-1]
    return shifted_str