
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    # Convert the integer to a string to work with its digits
    x_str = str(x)
    n = len(x_str)
    
    # If shift is greater than the number of digits, reverse the digits
    if shift > n:
        return x_str[::-1]
    
    # Perform the circular shift
    shift = shift % n  # In case shift is larger than n, normalize it
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    return shifted_str
