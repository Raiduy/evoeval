
def circular_shift(x, shift):
    x_str = str(x)
    if shift > len(x_str):
        return x_str[::-1]
    elif shift == len(x_str):
        return x_str
    else:
        first_part = x_str[:-shift]
        second_part = x_str[-shift:]
        result = second_part[::-1] + first_part[::-1]
        return result