def circular_shift(x, shift, direction):
    if not isinstance(x, int) or x < 0 or (not isinstance(shift, int)) or (shift < 0) or (direction not in ['R', 'L']):
        return 'Invalid Input'
    x = str(x)
    if shift > len(x):
        return x[::-1]
    if direction == 'R':
        return x[-shift:] + x[:-shift]
    else:
        return x[shift:] + x[:shift]