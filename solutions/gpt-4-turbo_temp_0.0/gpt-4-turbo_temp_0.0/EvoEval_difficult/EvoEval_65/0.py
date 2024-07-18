def circular_shift(x, shift, direction):
    if not isinstance(shift, int) or shift < 0 or direction not in ['R', 'L']:
        return 'Invalid Input'
    x_str = str(x)
    n = len(x_str)
    if shift > n:
        return x_str[::-1]
    if direction == 'R':
        result = x_str[-shift:] + x_str[:-shift]
    else:
        result = x_str[shift:] + x_str[:shift]
    return result