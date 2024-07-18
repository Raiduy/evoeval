def circular_shift(x, shift, direction):
    if not isinstance(shift, int) or shift < 0 or direction not in ['R', 'L']:
        return 'Invalid Input'
    x_str = str(x)
    if direction == 'R':
        return x_str[-shift:] + x_str[:-shift]
    else:
        return x_str[shift:] + x_str[:shift]