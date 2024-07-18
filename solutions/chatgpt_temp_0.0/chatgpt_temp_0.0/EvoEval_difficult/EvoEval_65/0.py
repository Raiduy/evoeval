def circular_shift(x, shift, direction):
    if not isinstance(shift, int) or shift <= 0 or direction not in ['R', 'L']:
        return 'Invalid Input'
    x_str = str(x)
    num_digits = len(x_str)
    if shift > num_digits:
        return x_str[::-1]
    if direction == 'R':
        shifted_str = x_str[-shift:] + x_str[:-shift]
    else:
        shifted_str = x_str[shift:] + x_str[:shift]
    return shifted_str