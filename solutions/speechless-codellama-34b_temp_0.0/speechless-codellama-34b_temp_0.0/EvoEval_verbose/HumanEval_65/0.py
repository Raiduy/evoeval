
def circular_shift(x, shift):
    x_str = str(x)
    if shift >= len(x_str):
        return x_str[::-1]
    elif shift == len(x_str):
        return x_str
    else:
        shifted_digits = x_str[-shift:]
        remaining_digits = x_str[:-shift]
        result = shifted_digits + remaining_digits
        return result