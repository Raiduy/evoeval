def circular_shift(x, shift, direction):
    if not isinstance(shift, int) or shift < 0 or (not isinstance(x, int)) or (x < 0):
        return 'Invalid Input'
    if direction not in ['R', 'L']:
        return 'Invalid Input'
    x_str = str(x)
    if shift >= len(x_str):
        return x_str[::-1]
    if direction == 'R':
        return x_str[-shift:] + x_str[:-shift]
    else:
        return x_str[shift:] + x_str[:shift]